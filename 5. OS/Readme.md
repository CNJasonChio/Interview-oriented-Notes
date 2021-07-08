# 计算机网络

> 特别鸣谢小林coding的图解系统系列

## 硬件结构

## 操作系统结构

## 内存管理

## 调度算法

## 文件系统

## 设备管理

## 网络系统

## 其他

### 有名管道与无名管道

#### 参考资料

1. [无名管道与有名管道_车小猿的博客-CSDN博客](https://blog.csdn.net/weixin_44522306/article/details/89475859)

### 最多能创建多少个 TCP 连接？

**最多65535个TCP连接肯定不对的！**

<img src="http://image.961110.xyz/images/2021/07/07/TCP4962e31619c82246.png" alt="TCP连接需要的资源" style="zoom:67%;" />

根据TCP连接需要的资源来判断可能的资源限制。

#### 端口号

![TCP四元组](http://image.961110.xyz/images/2021/07/07/640.webp)

端口号是16位，理论上有0 ~ 65535端口可以用，但是0-1023是系统保留端口号，所以只有部分端口用户可用。使用`cat /proc/sys/net/ipv4/ip_local_port_range`可以查询

![image-20210531170926933](C:\Users\JasonChio\AppData\Roaming\Typora\typora-user-images\image-20210531170926933.png)在`/etc/sysctl.conf`中可以修改限制，添加一行记录`net.ipv4.ip_local_port_range = 60000 60009`，执行`sysctl -p /etc/sysctl.conf `使其生效。

建立一个 TCP 连接，需要将通信两端的套接字（socket）进行绑定，如下：

**源 IP 地址：源端口号 <---->  目标 IP 地址：目标端口号**

只要四元组不重复，端口号就可以重复使用。

#### 文件描述符

建立TCP连接后，返回对应的文件描述符，如果文件描述符资源不够用，也会报错。

linux 对可打开的文件描述符的数量分别作了三个方面的限制。

**系统级**：当前系统可打开的最大数量，通过 `cat /proc/sys/fs/file-max` 查看

**用户级**：指定用户可打开的最大数量，通过 `cat /etc/security/limits.conf `查看

**进程级**：单个进程可打开的最大数量，通过 `cat /proc/sys/fs/nr_open` 查看

![Linux文件描述符的数量限制](http://image.961110.xyz/images/2021/07/07/Linux.png)

同样可以对限制进行修改。

#### 线程

过多的TCP连接需要大量的线程维护，因此会导致TCP连接建立缓慢，甚至系统崩溃（**C10K 问题**，就是当服务器连接数达到 1 万且每个连接都需要消耗一个线程资源时，操作系统就会不停地忙于线程的上下文切换，最终导致系统崩溃）

传统多线程并发模型中，每建一个TCP接就创建一个线程。现代并发模型支持 **IO 多路复用**的方式，简单说就是一个线程可以管理多个 TCP 连接的资源。

<img src="http://image.961110.xyz/images/2021/07/07/IO.webp" alt="IO多路复用" style="zoom:67%;" />

#### 内存

每一个TCP连接本身及其缓冲区都需要占用内存资源，过多的线程会内存溢出。

#### CPU

每一个TCP连接同样需要占用CPU资源，过多的TCP连接会增加CPU占用率

| **资源**        | **一台Linux服务器的资源** | **一个TCP连接占用的资源** | **占满了会发生什么**            |
| --------------- | ------------------------- | ------------------------- | ------------------------------- |
| **CPU**         | 看你花多少钱买的          | 看你用它干嘛              | 电脑卡死                        |
| **内存**        | 看你花多少钱买的          | 取决于缓冲区大小          | OOM                             |
| **临时端口号**  | ip_local_port_range       | 1                         | cannot assign requested address |
| **文件描述符**  | fs.file-max               | 1                         | too many open files             |
| **进程\线程数** | ulimit -n                 | 看IO模型                  | 系统崩溃                        |

#### 参考资料

1. [最多能创建多少个 TCP 连接？](https://mp.weixin.qq.com/s/HlSH2rxP4AhzIh0o3ZZU0Q)
2. [你管这破玩意叫 IO 多路复用?](https://mp.weixin.qq.com/s?__biz=Mzk0MjE3NDE0Ng==&mid=2247494866&idx=1&sn=0ebeb60dbc1fd7f9473943df7ce5fd95&chksm=c2c5967ff5b21f69030636334f6a5a7dc52c0f4de9b668f7bac15b2c1a2660ae533dd9878c7c&scene=21#wechat_redirect)

