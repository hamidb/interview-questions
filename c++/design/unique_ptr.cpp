#include <cstdlib>      /// nullptr_t
#include <utility>      /// swap

template<typename T>
class Unique_ptr {
private:
    T* _ptr;
public:
    // constexpr makes it a literal type so we can have A<shared_ptr<int>> a;
    constexpr Unique_ptr() noexcept = default;  // explicitly defaulted.
    
    // empty constructor. std::nullptr_t enables shared_ptr<int> A(0) or A(nullptr) 
    constexpr Unique_ptr(std::nullptr_t) noexcept {};  
    
    // raw pointer constructor.
    Unique_ptr(T* ptr) noexcept : 
    _ptr(ptr) {};
    
    // copy constructor.
    Unique_ptr(const Unique_ptr& ptr) = delete;
    
    // assignment operator
    Unique_ptr& operator=(const Unique_ptr& ptr) = delete;
    
    // move constructor.
    Unique_ptr(Unique_ptr&& ptr) {
        reset(ptr.release());
    }
    
    // destructor
    ~Unique_ptr() noexcept {
        if (_ptr)
            delete _ptr;
    }
    
    // move assignmnet operator.
    Unique_ptr& operator=(Unique_ptr&& ptr) {
        reset(ptr.release());
        return *this;
    }
    
    
    T& operator*() const {
        return *_ptr;    
    }
    
    T* operator->() const {
        return _ptr;    
    }
    
    explicit operator bool() const noexcept {
        return (_ptr) ? true : false;
    }
    
    T* get() const {
        return _ptr;    
    }
    
    void swap(Unique_ptr& ptr) noexcept {
        std::swap(_ptr, ptr._ptr);
    }
    
    T* release() noexcept
    {
        T* cp = _ptr;
        _ptr = nullptr;
        return cp;
    }
    
    void reset(T* ptr = nullptr) noexcept {
        Unique_ptr tmp{ptr};
        tmp.swap(*this);
    }
    
};

struct D
{
    D() { std::cout << "D::D" << std::endl; }
    ~D() { std::cout << "D::~D" << std::endl; }
    void bar() { std::cout << "D::bar" << std::endl; }
};

int main()
{
    std::cout << "\nExclusive ownership semantics demo\n";
    {
        Unique_ptr<D> up(new D()); // up is a unique_ptr that owns a D
        auto p = up.release(); // up releases ownership to p
        assert(!up); // now up owns nothing and holds a null pointer
        p->bar(); // and p owns the D object
        up.reset(p); // up regains ownership from p
    } // ~D called here
}
