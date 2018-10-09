'''
### 装饰器(Decrator)
- 在不改动函数代码的基础上无限制扩展函数功能的一种机制，本质上讲，装饰器是一个返回函数的高阶函数
- 装饰器的使用： 使用@语法， 即在每次要扩展到函数定义前使用@+函数名
'''

# 任务：
# 对hello函数进行功能扩展，每次执行hello万打印当前时间

import time

# 高阶函数，以函数作为参数
def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time: ", time.ctime())
        return f(*args, **kwargs)
    return wrapper


# 上面定义了装饰器，使用的时候需要用到@， 此符号是python的语法糖
@printTime
def hello():
    print("Hello world")
hello()

# 上面对函数的装饰使用了系统定义的语法糖
# 下面开始手动执行下装饰器
# 先定义函数

def hello3():
    print("我是手动执行的")
hello3()

hello = printTime(hello3)
hello()
print('******')

f= printTime(hello3)
f()