# vector内存管理

### 内存管理

`vecctor`在标准模板库中属于顺序容器，相当于一个会自动增长的数组。

#### 内存分配

##### 分配规则

两个成员函数：

1. `capacity`：对象缓冲区实际申请的空间的大小，可以理解成当前容器的容量（还可以继续扩大），初始为 0，push第一个元素增加为 1；
2. `size`：当前对象缓冲区存储数据的个数，可以理解成当前元素的数量；

`capacity`大于等于`size`，当两者相等的时候，`vector`就会扩容：

重新申请一块内存->把原有元素拷贝到新内存->放入新元素->释放掉原有内存

为了避免频繁扩容，每次扩容的时候 VS 都是以 1.5 倍扩大，gcc 是以 2 倍扩大

##### 为什么是成倍增长并且倍数是两倍

成倍增长的原因在于 n 次`push_back()`时间复杂度均摊为 O(1)

以固定值增长的方式，n 次`push_back()`时间复杂度均摊为 O(n)

当以 2 倍的方式扩容时，下一次申请的内存必然大于之前分配内存的总和，导致之前分配的内存不能再被使用，所以倍增因子最好在 1-2 之间，而3 4倍扩容会导致更多的空间浪费。

#### 内存释放

##### 释放方法

`vector.clear()`和`vector.erase()`都是减少了 size，而capacity并没有变化。

可用的释放方法：

```c++
template <class T>
void ClearVector(vector<T>& vt ) {
    vector<T> vtTemp; 
    veTemp.swap( vt );
}
// 或者
vector<Point>().swap(pointVec);
// 或者
pointVec.swap(vector<Point> ())
```

原理都是通过构造一个临时的vector对象，然后与原对象交换，原来vector占用的空间就等于一个默认构造的对象的大小，临时对象就具有原来对象v的大小，而该临时对象随即就会被析构，从而其占用的空间也被释放。

##### shrink_to_fit()函数

将vector调整到合适的大小，如果先clear清空元素，再调用shrink_to_fit，同样可以回收内存

##### vector中存放的是指针

vector销毁时，vector中指针指向的对象并不会被销毁，所以在程序退出或者根据需要手动释放

```
for (vector<void *>::iterator it = v.begin(); it != v.end(); it ++) {
    if (NULL != *it) {
        delete *it; 
        *it = NULL;
    }
}
```

#### 优化

针对大量数据的push_back操作，尽量提前使用`reverse()`提前设定容量大小，避免频繁的扩容

#### 参考链接

1. [vector扩容原理说明](https://blog.csdn.net/yangshiziping/article/details/52550291?utm_medium=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromMachineLearnPai2~default-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromMachineLearnPai2~default-2.control)
2. [C++ STL 中 vector 内存用尽后, 为什么每次是 2 倍的增长, 而不是 3 倍或其他值? ](https://www.zhihu.com/question/36538542)
3. [C++ vector 内存分配与回收机制](https://blog.csdn.net/qq_30835655/article/details/60762196)
4. [C++ STL ：Vector内存分配与释放](https://zhuanlan.zhihu.com/p/338390842)
5. [stl源码分析之vector](https://www.cnblogs.com/coderkian/p/3888429.html)

