# memmove 和 memcpy的区别以及memccpy

## 目录 or TODO

- [x] 1. memcpy
- [x] 2. memmove
- [x] 3. memccpy
- [x] 4. 参考链接

## 正文

### 1. memcpy

`memcpy()` 和 `memmove()`都是 C 语言中的库函数，在头文件 `string.h` 中，作用是拷贝一定长度的内存的内容，原型分别如下：

```c++
void *memcpy(void *dst, const void *src, size_t count);
void *memmove(void *dst, const void *src, size_t count);
```

他们的作用是一样的，都是返回一个指向 `dest` 的指针。唯一的区别是，**当内存发生局部重叠的时候，`memmove` 保证拷贝的结果是正确的，`memcpy` 不保证拷贝的结果的正确。**

<img src="http://image.961110.xyz/images/2021/07/15/memcpy.png" alt="memcpy内存重叠问题" style="zoom: 67%;" />

`memcpy()`在情况二会发生错误。`memmove`在情况二的时候，会从后往前拷贝。

### 2. memmove

```c++
void* __cdecl memmove(void* dst, const void* src, size_t count)
{
	void* ret = dst;
	if (dst <= src || (char*)dst >= ((char*)src + count)) {
		// 没有重叠，则从低到高拷贝
		while (count--) {
			*(char*)dst = *(char*)src;
			dst = (char*)dst + 1;
			src = (char*)src + 1;
		}
	}
	else {
		// 有重叠，则从高到拷贝
		dst = (char*)dst + count - 1;
		src = (char*)src + count - 1;
		while (count--) {
			*(char*)dst = *(char*)src;
			dst = (char*)dst - 1;
			src = (char*)src - 1;
		}
	}

	return(ret);
}
```

### 3. memccpy

原型：
`extern void *memccpy(void *dest, void *src, unsigned char ch, unsigned int count);`

遇到字符 `ch` 则停止复制。

返回指向字符 `ch` 后的第一个字符的指针，如果 `src` 前 n 个字节中不存在 `ch` 则返回 NULL。

### 4. 参考链接

1. [MyBlog/memcpy与memmove区别和实现.md](https://github.com/SigalHu/MyBlog/blob/master/C%2B%2B/memcpy与memmove区别和实现.md)；
2. [memmove 和 memcpy的区别以及处理内存重叠问题](https://blog.csdn.net/Li_Ning_/article/details/51418400)
