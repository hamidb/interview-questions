#include <iostream>
#include <string>
#include <vector>

// forward declare
template<class T, int N>
class RingIterator;

template<class T, int N>
class RingBuffer {
  public:      
    // iterator typedefs
    using iterator = RingIterator<T, N>;

    RingBuffer(): _size(0), _begin_idx(0) {}
    friend class RingIterator<T, N>;
    iterator begin() {
        return iterator(*this, 0);
    }
    iterator end() {
        return iterator(*this, _size);
    }
    void push_back(const T &item) {
        _buffer[end_idx()] = item;
        if (_size < N) {
            _size++;
        } else {
            _begin_idx = (_begin_idx+1) % N;
        }
    }
    T& pop_front() {
        // assert(_size > 0)
        T& tmp = _buffer[_begin_idx];
        _begin_idx = (_begin_idx+1) % N;
        _size--;
        return tmp;
    }
    int end_idx() {
        return (_begin_idx + _size) % N;
    }

  private:
    T _buffer[N];
    int _size;
    int _begin_idx;
};

template<class T, int N>
class RingIterator {
  public:
    using reference = T&;
    using iterator = RingIterator<T, N>;
    // _rb(rb) will avoid copying.
    RingIterator(RingBuffer<T, N> &rb, int off): _rb(rb), _off(off) {}

    iterator& operator++() {  // prefix ++
        _off++;
        return *this;
    }
    iterator& operator++(int) {  // postfix ++
        iterator tmp = *this;
        ++(*this);
        return tmp;
    }
    iterator& operator--() {  // prefix --
        _off--;
        return *this;
    }
    iterator& operator--(int) {  // postfix --
        iterator tmp = *this;
        --(*this);
        return tmp;
    }
    iterator& operator+=(int value) {
        _off += value;
        return *this;
    }
    iterator& operator-=(int value) {
        _off -= value;
        return *this;
    }
    bool operator!=(const iterator& rhs) {
        return (_off != rhs._off);
    }
    bool operator==(const iterator& rhs) {
        return (_off == rhs._off);
    }
    const reference operator[] (int index) {
        // assert(index >= 0);
        // assert(index < _rb._size);
        return _rb._buffer[(_rb._begin_idx + _off + index) % N];
    }
    
  private:
    RingBuffer<T, N> _rb;
    int _off;
};

int main()
{
    RingBuffer<int, 5> ring;
    ring.push_back(1);
    ring.push_back(2);
    std::cout << ring.pop_front() << std::endl;
    for (int i=0; i < 4; ++i) {
        ring.push_back(i);
    }
    std::cout << "let's iterate..." << std::endl;
    RingIterator<int, 5> it = ring.begin();
    for ( ; it != ring.end(); ++it) {
        std::cout << it[0] << std::endl;
    }
    
    // output:
    // 1
    // let's iterate...
    // 2
    // 0
    // 1
    // 2
    // 3

}
