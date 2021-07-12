# 数据结构和算法

## 目录 or TODO

1. [十大排序算法](https://github.com/CNJasonChio/Interview-oriented-Notes/blob/master/1.%20Algorithm/1.%20%E5%8D%81%E5%A4%A7%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95.md)
2. [进制转换类题目](https://github.com/CNJasonChio/Interview-oriented-Notes/blob/master/1.%20Algorithm/2.%20%E8%BF%9B%E5%88%B6%E8%BD%AC%E6%8D%A2.md)
3. 数组
4. 链表
5. [二叉树](https://github.com/CNJasonChio/Interview-oriented-Notes/blob/master/1.%20Algorithm/5.%20%E4%BA%8C%E5%8F%89%E6%A0%91.md)
6. B 树
7. 哈希表
8. [摩尔投票算法](https://github.com/CNJasonChio/Interview-oriented-Notes/blob/master/1.%20Algorithm/8.%20%E6%91%A9%E5%B0%94%E6%8A%95%E7%A5%A8%E7%AE%97%E6%B3%95.md)

### [十大排序算法](https://github.com/CNJasonChio/Interview-oriented-Notes/blob/master/1.%20Algorithm/1.%20%E5%8D%81%E5%A4%A7%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95.md)

1. 直接插入排序
2. 希尔排序
3. 冒泡排序
4. 快速排序
5. 直接选择排序
6. 堆排序
7. 归并排序
8. 计数排序
9. 桶排序
10. 基数排序

#### 总结

| 排序算法 | 平均时间复杂度 | 最好情况   | 最坏情况   | 空间复杂度 | 稳定性   |
| :------- | :------------: | :--------- | :--------- | :--------- | :------- |
| 冒泡排序 |     O(n^2)     | O(n)       | O(n^2)     | O(1)       | 稳定     |
| 插入排序 |     O(n^2)     | O(n)       | O(n^2)     | O(1)       | 稳定     |
| 希尔排序 |    O(n^1.3)    | O(n)       | O(n^2)     | O(1)       | 不稳定   |
| 选择排序 |     O(n^2)     | O(n^2)     | O(n^2)     | O(1)       | 不稳定?  |
| 快速排序 |   O(n*log n)   | O(n*log n) | O(n^2)?    | O(log n)   | 不稳定？ |
| 归并排序 |   O(n*log n)   | O(n*log n) | O(n*log n) | O(1)?      | 稳定     |
| 堆排序   |  O(n*log n)？  | O(n*log n) | O(n*log n) | O(1)?      | 不稳定？ |
| 计数排序 |    O(n+k)?     | O(n+k)     | O(n+k)     | O(k)?      | 稳定?    |
| 桶排序   |    O(n+k)?     | O(n+k)     | O(n^2)?    | O(n+k)     | 稳定？   |
| 基数排序 |    O(n*k)？    | O(n*k)     | O(n*k)     | O(n+k)     | 稳定？   |

- n -- 数据规模
- k -- “桶的个数

### [进制转换类题目](https://github.com/CNJasonChio/Interview-oriented-Notes/blob/master/1.%20Algorithm/2.%20%E8%BF%9B%E5%88%B6%E8%BD%AC%E6%8D%A2.md)

### 数组	

#### 双指针（快慢指针）

对数组或者链表进行操作时，可以考虑一下双指针法能不能运用。

例题：[977. 有序数组的平方 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)

#### 滑动窗口



#### 二分查找	

##### 关键问题

1. 数组有序；
2. 数组中无重复元素，否则返回结果可能不唯一；
3. 左闭右闭或者左闭右开原则：在循环中对边界的更新要一直秉持相同的原则

#### 充当哈希表

当元素的范围比较小，比如十以内数字、大小写英文字母等，统计元素出现次数时，可以用数组充当哈希表，加快处理速度。

### 链表

#### 常用技巧

1. dummy节点，可以避免对头结点的特殊处理；
2. 快慢指针：倒数第几个节点。。。

### [二叉树](https://github.com/CNJasonChio/Interview-oriented-Notes/blob/master/1.%20Algorithm/5.%20%E4%BA%8C%E5%8F%89%E6%A0%91.md)

#### 遍历

三者以一种统一的框架进行编写：

1. 统一用`current`指针开启循环，并进行遍历；
2. 统一循环结束条件：`while(!stk.empty() || current!=nullptr)`;

##### 前序遍历和中序遍历

只是单纯的处理节点的位置不同。

##### 后序遍历

**左右中**

- 增加了`last`节点防止因右节点重复访问而陷入死循环；
- **节点访问过后要将其赋为空指针，开启下一次循环；**

#### 二叉搜索树



#### 完全二叉树



#### 红黑树

### B 树

### 哈希表

#### 常用技巧

1. 统计出现次数；
2. 结果是否出现；

#### 底层原理

#### 哈希碰撞的解决方法



###  [摩尔投票算法](https://github.com/CNJasonChio/Interview-oriented-Notes/blob/master/1.%20Algorithm/8.%20%E6%91%A9%E5%B0%94%E6%8A%95%E7%A5%A8%E7%AE%97%E6%B3%95.md)

### 前缀和
