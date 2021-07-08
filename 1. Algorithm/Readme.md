# 数据结构和算法

### 十大排序算法

#### 插入排序法

##### 直接插入排序



##### 希尔排序

#### 交换排序法

##### 冒泡排序

##### 快速排序

#### 选择排序法

##### 直接选择排序

##### 堆排序

#### 归并排序法

##### 归并排序

#### 分布排序法

##### 计数排序

##### 桶排序

##### 基数排序

#### 总结

| 排序算法 | 平均时间复杂度 | 最好情况   | 最坏情况   | 空间复杂度 | 稳定性   |
| -------- | :------------: | ---------- | ---------- | ---------- | -------- |
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

#### 参考链接

1. [图解大顶堆的构建、排序过程 - 小黑a电脑 (xiaoheidiannao.com)](https://www.xiaoheidiannao.com/7436.html)
2. [图解排序算法(三)之堆排序 - dreamcatcher-cx - 博客园 (cnblogs.com)](https://www.cnblogs.com/chengxiao/p/6129630.html)

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

### 二叉树

#### 遍历

三者以一种统一的框架进行编写：

1. 统一用current指针开启循环，并进行遍历；
2. 统一循环结束条件：`while(!stk.empty() || current!=nullptr)`;

##### 前序遍历

**中左右**

```c++
std::vector<int> BinTreeTraversal::PostorderTraversal(TreeNode* root){
    if(root==nullptr)
        return {};
    std::vector<int> result;
    std::stack<int> stk;

    TreeNode* current = root;
    while(!stk.empty() || current!=nullptr){
        while(current!=nullptr){   
            result.push_back(current->val);	// 先将访问到的节点放到result中，再入栈
            stk.push(current);	            // 中
            current = current->left;		// 左
        }
        current = stk.top();
        stk.pop();
        // 右
        current = current ->right;
    }
    return result;
}
```

##### 中序遍历

**左中右**

```c++
std::vector<int> BinTreeTraversal::PostorderTraversal(TreeNode* root){
    if(root==nullptr)
        return {};
    std::vector<int> result;
    std::stack<int> stk;
    TreeNode* current = root;
    while(!stk.empty() || current!=nullptr){
        while(current!=nullptr){
            stk.push(current);
            current = current->left;	// 左
        }
        current = stk.top();        	// 中
        stk.pop();
        result.push_back(current->val);
        current = current ->right;		// 右
    }
    return result;
}
```

##### 后序遍历

**左右中**

- 增加了last节点防止因右节点重复访问而陷入死循环；
- **节点访问过后要将其赋为空指针，开启下一次循环；**

```c++
std::vector<int> BinTreeTraversal::PostorderTraversal(TreeNode* root){
    if(root==nullptr)
        return {};
    std::vector<int> result;
    std::stack<int> stk;
    TreeNode* current = root, last = nullptr;
    while(!stk.empty() || current!=nullptr){
        while(current!=nullptr){
            stk.push(current);
            current = current->left;	// 左
        }
        current = stk.top();        	// 仅取栈顶，而不推出
        // 右节点不为空且上没有访问过
        if(current->right!=nullptr && last != current->right){
            current = current->right;            // 右
        }
        else{
            result.push_back(current->val);		// 中
            stk.pop();
            last = current;		// 记录最近访问过的节点
            current = nullptr;	// current此时是叶子节点，赋空开启下一次循环
        }
    }
    return result;
}
```

#### 二叉搜索树



#### 完全二叉树



#### 红黑树



#### B树



### 哈希表

#### 常用技巧

1. 统计出现次数；
2. 结果是否出现；

#### 底层原理

##### 哈希碰撞的解决方法



##### 底层实现
