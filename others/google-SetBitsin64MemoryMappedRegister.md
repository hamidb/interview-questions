Set or Clear Bits in a 64-bits Memory Mapped Register
=====================================================

Write a function that sets/clears bits from a memory mapped 64 bit register. Function receives starting bit and number of bits to set/clear, without touching other bits

### Example:
```
Start: 5, Len: 2
0000 0000 -> 0011 0000
```

Solution
========
```c++
  void setBits(size_t start, size_t len) {
    volatile unsigned char* _register = (unsigned char*) 0xfff1234;
    int64_t result = (int64_t) *_register;
    int64_t mask = 2^len;
    mask <<= start-1;
    result |= mask;
    *_register = result;
  }
```
