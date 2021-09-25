# Jason-网易互娱-游戏开发工程师

### 一面（9.24）

1. 半个小时先做一道题

   ```shell
   给你一个很长的数字回文串 num，返回大于 num，由相同数字重新组合而成的最小回文串。如果不存在这样的回文串，则返回空串""。
   回文串是正读和反读都一样的字符
   示例1：输入：num="1221"	输出："2112"	解释：下个比"1221"大的回文串是"2112"
   示例2：输入：num="32123"	输出：""	解释：不存在通过重组"32123"的数字可得比"32123"还大的回文串。
   示例3：输入：num="45544554"	输出："54455445"	解释：下个比"45544554"还要大的回文串是"54455445"
   
   提示 1<=num.length<=105, num是回文串。
   ```

   只会回溯法剪枝

2. 项目问题

3. 为什么选择 flask

4. 为什么选择 MySQL，不选择mango

5. 手写 CRUD，按页排序

6. flask如何保障多线程一致性问题

7. 常用的 Linux 命令

8. top命令如何查看系统负载怎么样（不清楚）

9. define 和 inline，两者都定义了一个函数，哪个更快

10. inline修饰的函数一定是inline的吗，什么时候不是

11. 类的大小

    ```C++
    #include <iostream>
    using namespace std;
    class A {
    private:
        char a;
        int b;
        char c;
        static int d;
        const int g = 0;
        char *s;
    public:
        virtual void f() {};
        virtual void f1() {};
        void f2() {};
        virtual void f3() = 0;
    };
    int main() {
        cout << sizeof(A) << endl;	// 32(64位机器下)
        return 0;
    }
    ```

12. 64位机器下，long和int的大小都是多大，范围一样吗

13. static const int o = 1; 存放在哪里，是否占用类的空间

14. f()和f3()有什么区别（虚函数和纯虚函数的区别，忘记了）

15. 虚函数是怎么实现的

16. C++内存从低地址到高地址分别有哪些分区（没有注意地址的高低顺序）

17. 智能指针

18. 手动实现shared_ptr（不会）

19. 如何实现一个key-value的数据结构，其插入、删除、查找、随机返回都是O(1)的复杂度（已经被打懵了，完全没有思路）

    1. insert(int k, int v)
    2. delete(int k)
    3. find(int k)
    4. get_random()-> k, v

20. ```
    [A, B, time1]
    [B, C, time2]
    [A, C, time3]
    表示 A, B 认识的时间为 time1
    表示 B, C 认识的时间为 time2
    表示 A, C 认识的时间为 time3
    A, B认识，B, C认识，则 A, C 就认识（朋友的朋友就是朋友）
    
    计算所有人都互相认识的最早时间
    ```

    面试官提示先针对数据做排序

21. 平时玩儿什么游戏吗
