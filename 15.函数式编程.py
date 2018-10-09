'''
## 函数式编程(FunctionalProgramming)
- 基于lambda演算的一种编程方式
- 程序中只有函数
- 函数可以作为参数，同样可以作为返回值
- 纯函数式编程语言： LISP， Haskell

- Python函数式编程只是借鉴函数式编程的一些特点，可以理解成一半函数式一半Python
- 需要讲述
- 高阶函数
- 返回函数
- 匿名函数
- 装饰器
- 偏函数

###  lambda表达式
- 函数： 最大程度复用代码
    - 存在问题： 如果函数很小，很短，则会造成啰嗦
    - 如果函数被调用次数少，则会造成浪费
    - 对于阅读者来说，造成阅读流程的被迫中断

- lambda表达式（匿名函数）：
    - 一个表达式，函数体相对简单
    - 不是一个代码块，仅仅是一个表达式
    - 可以有参数，有多个参数也可以，用逗号隔开
'''


# lambda表达式的用法
# 1. 以lambda开头
# 2. 紧跟一定的参数（如果有的话）
# 3. 参数后用冒号和表达式主题隔开
# 4. 只是一个表达式，所以，没有return

# 计算一个数字的100倍数
# 因为就是一个表达式，所以没有return
stm = lambda x: 100 * x
# 使用上跟函数调用一模一样
a=stm(89)
print(a)

stm2 = lambda x,y,z: x+ y*10 + z*100
a2=stm2(4,5,6)
print(a2)

#高阶函数
#把函数作为参数使用的函数，叫高阶函数

# 变量可以赋值
a = 100
b = a


# 函数名称就是一个变量
def funA():
    print("In funA")
funB = funA
funB()

# 高阶函数举例
# funA是普通函数，返回一个传入数字的100倍数字

def funA(n):
    return n * 100

def funC(n, f):
    # 假定函数是把n扩大100被
    return f(n) * 3

a=funC(9, funA)
print( a )


#系统高阶函数-map
#原意就是映射，即把集合或者列表的元素，每一个元素都按照一定规则进行操作，生成一个新的列表或者集合
#map函数是系统提供的具有映射功能的函数，返回值是一个迭代对象


# 有一个列表，想对列表里的每一个元素乘以10， 并得到新的列表
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i * 10)
print(l2)

# 利用map实现
def mulTen(n):
    return n*10
l3 = map(mulTen, l1 )
# map类型是一个可迭代的结构，所以可以使用for遍历
for i in l3:
    print(i)


# reduce
'''
- 原意是归并，缩减
- 把一个可迭代对象最后归并成一个结果
- 对于作为参数的函数要求： 必须有两个参数，必须有返回结果
- reduce([1,2,3,4,5]) == f( f(f(f(1,2),3), 4),5)
- reduce 需要导入functools包
'''

from functools import reduce

# 定义一个操作函数
# 加入操作函数只是相加
def myAdd(x, y):
    return x + y
# 对于列表[1,2,3,4,5,6]执行myAdd的reduce操作
rst = reduce(myAdd, [1, 2, 3, 4, 5, 6])
print(rst)

