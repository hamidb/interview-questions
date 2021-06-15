#include <cstdlib>      /// nullptr_t
#include <atomic>       /// atomic
#include <utility>      /// swap

template<typename T>
class Shared_ptr {
private:
    T* _ptr;
    std::atomic<long>* _ref_count;  // atomic for race conditions.
public:
    // constexpr makes it a literal type so we can have A<shared_ptr<int>> a;
    constexpr Shared_ptr() noexcept = default;  // explicitly defaulted.
    
    // empty constructor. std::nullptr_t enables shared_ptr<int> A(0) or A(nullptr) 
    constexpr Shared_ptr(std::nullptr_t) noexcept {};  
    
    // raw pointer constructor.
    Shared_ptr(T* ptr) noexcept : 
    _ptr(ptr),
    _ref_count(new std::atomic<long>{1}) {};
    
    // copy constructor.
    Shared_ptr(const Shared_ptr& ptr) :
    _ptr(ptr._ptr),
    _ref_count(ptr._ref_count) {
        if (_ptr) ++(*_ref_count);
    }
    
    // move constructor.
    Shared_ptr(Shared_ptr&& ptr) {
        _ptr = std::move(ptr._ptr);
        _ref_count = std::move(ptr._ref_count);
        ptr._ptr = nullptr;
        ptr._ref_count = nullptr;
    }
    
    // destructor
    ~Shared_ptr() noexcept {
        free();
    }
    
    // move assignmnet operator.
    Shared_ptr& operator=(Shared_ptr&& ptr) {
        free();
        _ptr = std::move(ptr._ptr);
        _ref_count = std::move(ptr._ref_count);
        ptr._ptr = nullptr;
        ptr._ref_count = nullptr;
    }
    
    // assignment operator
    Shared_ptr& operator=(const Shared_ptr& ptr) {
        // copy and swap.
        Shared_ptr tmp(ptr);
        tmp.swap(*this);
        return *this;
    }
    
    T& operator*() const {
        return *_ptr;    
    }
    
    T* operator->() const {
        return _ptr;    
    }
    
    T* get() const {
        return _ptr;    
    }
    
    long use_count() {
        if (_ref_count)
            return *_ref_count;
        else
            return 0;
    }
    void swap(Shared_ptr& ptr) noexcept {
        std::swap(_ptr, ptr._ptr);
        std::swap(_ref_count, ptr._ref_count);
    }
    
    void reset() noexcept {
        Shared_ptr tmp{};
        tmp.swap(*this);
    }
    
    void free() {
        if (_ref_count) {
            if (--(*_ref_count) == 0) {
                delete _ref_count;
                if (_ptr)
                    delete _ptr;
            }
        }
    }
};

struct Base
{
    Base() { std::cout << "  Base::Base()\n"; }
    // Note: non-virtual destructor is OK here
    // See https://stackoverflow.com/questions/3899790/shared-ptr-magic
    ~Base() { std::cout << "  Base::~Base()\n"; }
};
 
struct Derived: public Base
{
    Derived() { std::cout << "  Derived::Derived()\n"; }
    ~Derived() { std::cout << "  Derived::~Derived()\n"; }
};
 
void thr(Shared_ptr<Base> p)
{
    std::this_thread::sleep_for(std::chrono::seconds(1));
    Shared_ptr<Base> lp = p; // thread-safe, even though the
                             // shared use_count is incremented
    {
        static std::mutex io_mutex;
        std::lock_guard<std::mutex> lk(io_mutex);
        std::cout << "local pointer in a thread:\n"
                  << "  lp.get() = " << lp.get()
                  << ", lp.use_count() = " << lp.use_count() << '\n';
    }
}
int main()
{
    Shared_ptr<Base> p(new Derived());
 
    std::cout << "Created a shared Derived (as a pointer to Base)\n"
              << "  p.get() = " << p.get()
              << ", p.use_count() = " << p.use_count() << '\n';
    std::thread t1(thr, p), t2(thr, p), t3(thr, p);
    p.reset(); // release ownership from main
    std::cout << "Shared ownership between 3 threads and released\n"
              << "ownership from main:\n"
              << "  p.get() = " << p.get()
              << ", p.use_count() = " << p.use_count() << '\n';
    t1.join(); t2.join(); t3.join();
    std::cout << "All threads completed, the last one deleted Derived\n";
}
