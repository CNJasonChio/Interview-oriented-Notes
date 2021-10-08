# call_once
## 目录 or TODO
- [x] 1.让任务只执行一次
- [x] 2.参考链接
## 正文

### 1. 让任务只执行一次

#### 1.1. 函数定义

使用头文件 <mutex> 中的 `std::call_once()`，确保函数在多线程环境下只被执行一次

```c++
// 函数原型
template< class Callable, class... Args >
void call_once( std::once_flag& flag, Callable&& f, Args&&... args );
```

- flag：once_flag 类型的对象，要保证这个对象能够被多个线程同时访问到
- f：回调函数，可以传递一个有名函数地址，也可以指定一个匿名函数
- args：作为实参传递给回调函数

#### 1.2. 使用方法

```c++
#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

once_flag g_flag;

void do_once(int a, string b) {
    cout << "name: " << b << ", age: " << a << endl;
}

void do_something(int age, string name) {
    static int num = 1;
    call_once(g_flag, do_once, 19, "luffy");
    cout << "do_something() function num = " << num++ << endl;
}

int main() {
    thread t1(do_something, 20, "ace");
    thread t2(do_something, 20, "sabo");
    thread t3(do_something, 19, "luffy");
    t1.join();
    t2.join();
    t3.join();

    return 0;
}

// 输出结果
name: luffy, age: 19
do_something() function num = 1
do_something() function num = 2
do_something() function num = 3
```

### 2. 参考链接

1. [call_once](https://subingwen.cn/cpp/call_once/)

