# Jason-Soul-C++

### 一面（9.5）

1. 滴滴的项目，介绍了Ray

2. 智能指针

3. 内存池

4. 多态的实现

5. 进程和线程的区别

6. 锁的概念（需要多了解）

7. 进程间的通信方式

8. 内核态和用户态（说的不是很清楚）

9. 场景题：

   1. 系统发生错误后会钉钉报警（http请求实现），高并发场景下高频繁的报警极为耗费性能，并且也不需要那么多的报警。请考虑对报警实现一个频控，在指定时间内达到多少次后进行报警，例如1分钟之内100次报警后才真正报警一次）

      ```java
      try {
      
      } catch (Exceptione) {
      	void alert(String message){}
      }
      ```

      没答出来，面试官说用队列和时间戳来实现

10. 反问

    1. 部门业务：广告投放
