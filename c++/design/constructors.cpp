class String {
private:
    char* mData;
    size_t mSize;
public:
    // default constructor.
    String() : mData(nullptr), mSize(0) {
        std::cout << "default constructor" << std::endl;
    }
    
    // destructor.
    ~String() {
        std::cout << "destructor" << std::endl;
        if (mData != nullptr)
            delete[] mData;
    }
    
    // copy constructor.
    String(const String& other) : mData(new char[other.mSize]), mSize(other.mSize) {
        std::cout << "copy constructor" << std::endl;
        memcpy(mData, other.mData, mSize);
    };
    
    // copy assignmnet operator.
    String& operator=(const String& other) {
        std::cout << "copy assignment" << std::endl;
        if (this != &other) {
            delete[] mData;
            mData = new char[other.mSize];
            mSize = other.mSize;
            memcpy(mData, other.mData, mSize);
        }
        return *this;
    }
    
    // move constructor:
    // 1. initialize empty this
    // 2. move other.members to this.members
    // 3. nullify other.members
    String(String&& other) noexcept : mData(nullptr), mSize(0) {
        std::cout << "move constructor" << std::endl;
        mData = other.mData;
        mSize = other.mSize;
        other.mData = nullptr;
        other.mSize = 0;
        // or simply *this = std::move(other);
    }
    
    // Move assignment operator:
    // 1. no operation if self assign.
    // 2. delete already existing data for this.
    // 3. move other.members to this.members
    // 4. nullify other
    // 5. return a reference to this.
    String& operator=(String&& other) {
        std::cout << "move assignment" << std::endl;
        if (this != &other) {
            delete[] mData;
            mData = other.mData;
            mSize = other.mSize;
            other.mSize = 0;
            other.mData = nullptr;
        }
        return *this;
    }
    
    // raw pointer constructor
    String(const char* str) {
        std::cout << "creating" << std::endl;
        mSize = strlen(str) + 1;
        mData = new char[mSize];
        memcpy(mData, str, mSize);
    }
    
    void print() {
        for (int i=0; i < mSize; ++i)
            printf("%c", mData[i]);
        printf("\n");
    }
};

class Entity {
public:
    Entity() = default;
    ~Entity() {}
    Entity(const String& str) : mStr(str) {
        std::cout << "copy" << std::endl;
    }
    Entity(String&& str) : mStr(std::move(str)) {
        std::cout << "move" << std::endl;
    }
    void print() {
        mStr.print();
    }
private:
    String mStr;
};

int main() {
    {
        String s0;  // default empty.
        String s1("Hamid");  // raw pointer constructor.
        String s2 = (String&&)"Bazargani";  // move assignment.
        s2.print();
        String s3 = std::move(s1);  // move assignment.
        String s4(s2);  // copy constructor.
    }
    {
        Entity e0("Hamid");  // move constructor.
        e0.print();
    }
}
