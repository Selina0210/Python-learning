# 把字符串转化成十进制数字
int("12345")

# 求八进制的字符串12345，表示成十进制的数字是多少
int("12345", base=8)

# 求十六进制的字符串12345，表示成十进制的数字是多少
def int16(x, base=16):
    return int(x, base)
int16("12345")

'''
### 偏函数
- 参数固定的函数，相当于一个有特定参数的函数体
- functools.partial的作用是，把一个函数某些参数固定，返回一个新函数
'''

import functools
#实现上面int16的功能
int16 = functools.partial(int, base=16)

int16("12345")