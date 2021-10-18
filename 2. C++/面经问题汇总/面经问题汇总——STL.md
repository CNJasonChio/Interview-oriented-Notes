# 面经问题汇总—STL
## 目录 or TODO
- [ ] 1.STL有哪些组件
- [ ] 2.常用容器
- [ ] 3.map和unorder_map有哪些区别,map为什么是log n的查询和修改时间
- [ ] 4.map中红黑树最长路径和最短路径的差值
- [x] 5.哈希表如何实现、哈希冲突
- [ ] 6.模板函数
- [x] 7.vector和list区别
- [x] 8.resize和reserve的区别
- [x] 9.vector中erase和remove
- [x] 10.vector内存管理
- [ ] 11.vector迭代器失效
- [ ] 12.STL中Set中存储一个类对象 如何设计？
- [ ] 13.双向queue的实现原理
## 正文

### 1. STL有哪些组件

<img src="https://images.961110.xyz/images/2021/09/27/STL.png" alt="STL六大组件" style="zoom: 33%;" />

[详细信息](https://github.com/jasonchio-cn/Interview-oriented-Notes/blob/master/2.%20C%2B%2B/STL%E5%85%AD%E5%A4%A7%E7%BB%84%E4%BB%B6/STL%E5%85%AD%E5%A4%A7%E7%BB%84%E4%BB%B6.md)

### 2. 常用容器

[详细信息](https://github.com/jasonchio-cn/Interview-oriented-Notes/blob/master/2.%20C%2B%2B/STL%E5%85%AD%E5%A4%A7%E7%BB%84%E4%BB%B6/7.%20STL%E5%AE%B9%E5%99%A8.md)

### 3. map和unorder_map有哪些区别,map为什么是log n的查询和修改时间

[详细信息](https://github.com/jasonchio-cn/Interview-oriented-Notes/blob/master/2.%20C%2B%2B/STL%E5%85%AD%E5%A4%A7%E7%BB%84%E4%BB%B6/7.%20STL%E5%AE%B9%E5%99%A8.md)

### 4. map中红黑树最长路径和最短路径的差值

[详细信息](https://github.com/jasonchio-cn/Interview-oriented-Notes/blob/master/2.%20C%2B%2B/STL%E5%85%AD%E5%A4%A7%E7%BB%84%E4%BB%B6/7.%20STL%E5%AE%B9%E5%99%A8.md)

### 5. 哈希表如何实现、哈希冲突

[详细信息](https://github.com/jasonchio-cn/Interview-oriented-Notes/blob/jason_dev/2.%20C%2B%2B/1.%20%E9%9D%A2%E7%BB%8F%E9%97%AE%E9%A2%98%E6%B1%87%E6%80%BB/%E5%93%88%E5%B8%8C%E8%A1%A8%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E3%80%81%E5%93%88%E5%B8%8C%E5%86%B2%E7%AA%81.md)

### 6. 模板函数

详细信息

### 7. vector和list区别



### 8. resize和reserve的区别

#### 8.1. resize和reserve区别

`reserve`增加了`vector`的`capacity`，但是它的`size`没有改变；`resize`改变了`vector`的`capacity`同时也增加了它的`size`，因为其在`resize`的时候新建了对象。

### 9. vector中erase和remove

#### 9.1. erase

`erase`删除容器中的一个或者一段元素。被删除元素之后的所有元素都向前移动，因此传入的迭代器指向没变，但是所指的元素已经发生了变化。其实`vector`还维持着一个`last`指针，开始的时候`=end`，随着删除，`last`前移，最终`vector`的`size`是`last-begin`，或者我们可以认为`end`值改变了，但最初传入的`end`没有变。

```c++
vector<int>::iterator itr = v.begin();
while (itr != v.end()) {
    if (*v == 1)
        v.erase(itr);
    itr++;//这里删除后迭代器会更新出错
}

// 正确写法
vector<int>::iterator itr = v.begin();
while (itr != v.end()) {
    if (*v == 1)
        v.erase(itr);
    else
        itr++;
}
```

#### 9.2. remove

将等于`value`的元素放到`vector`的尾部，但并不减少`vector`的`size`，返回新的`end()`值（非`val`部分的`end`）

#### 9.3. 二者结合使用

可以删除值为 x 的元素、

```c++
vec.erase(remove(vec.begin(), vec.end(), x), vec.end());
```

#### 9.4. 参考链接

1. [vector的remove和erase函数的区别](https://blog.csdn.net/xzymmd/article/details/83652726)

### 10. vector内存管理

[详细信息](https://github.com/jasonchio-cn/Interview-oriented-Notes/blob/jason_dev/2.%20C%2B%2B/1.%20%E9%9D%A2%E7%BB%8F%E9%97%AE%E9%A2%98%E6%B1%87%E6%80%BB/vector%E5%86%85%E5%AD%98%E7%AE%A1%E7%90%86.md)

### 11. vector迭代器失效

1. 详细作返回的迭代器肯定失效。
2. 当插入(push_back)一个元素后，capacity返回值与没有插入元素之前相比有改变，则需要重新加载整个容器，此时begin和end操作返回的迭代器都会失效。
3. 当进行删除操作（erase，pop_back）后，指向删除点的迭代器全部失效；指向删除点后面的元素的迭代器也将全部失效。

#### 11.1. 参考链接

1. [实战c++中的vector系列--可怕的迭代器失效之二（删除vector中元素）](https://dabaojian.blog.csdn.net/article/details/50334503)

### 12. STL中Set中存储一个类对象 如何设计？



### 13. 双向queue的实现原理

