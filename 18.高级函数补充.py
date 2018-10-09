# 1、Zip函数
# 将两个可迭代的内容生成一个可迭代的tuple元素类型组成的内容
# 案例，将姓名与成绩一一对应
l1 = ['Selina','Adele','Lili','Tom']
l2 = [97,88,75,66]
z=zip(l1,l2)
print(type(z))
print(z)
for i in z:
    print(i)

# enumerate
# 跟zip功能比较像
# 对可迭代对象里的每一元素，配上一个索引，然后索引和内容构成tuple类型
# 案例，给列表的每一个元素配上一个索引index，默认从0开始
l1 = [11,22,33,44,55]
em = enumerate(l1)
for i in em:
    print(i)

#索引从其他数据开始，利用start设置
em1 = enumerate(l1,start=88)
l2 = [i for i in em1]
print(l2)

'''
# collections模块
- namedtuple
- deque
'''

#namedtuple,是一个可命名的tuple
#案例
# 定义点坐标
import collections
Point = collections.namedtuple("Point", ['x', 'y'])  #点，xy轴
p = Point(11, 22) #实例化对象，一个x坐标为11，y坐标为22的点
print(p)

#定义圆
Circle = collections.namedtuple("Circle", ['x', 'y', 'r']) #圆，圆心坐标x y，和半径r
c = Circle(100, 150, 50) #实例化对象，一个圆心x坐标为100，y坐标为150，半径为50的圆
print(c)

# dequeue
# 比较方便的解决了频繁删除插入带来的效率问题
from collections import deque

q = deque(['a', 'b', 'c'])
print(q)

q.append("d")
print(q)

q.appendleft('x')
print(q)

# defaultdict
# 当直接读取dict不存在的属性时，直接返回默认值
from collections import defaultdict
# lambda表达式，直接返回字符串
func = lambda: "不存在"
d2 = defaultdict(func)

d2["one"] = 1
d2["two"] = 2

print(d2['one'])
print(d2['four'])

# Counter
# 统计字符串个数
from collections import Counter

# 为什么下面结果不把abcdefgabced.....作为键值，而是以其中每一个字母作为键值
# 需要括号里内容为可迭代
c = Counter("abcdefgabcdeabcdabcaba")
print(c)

s = ["liudana", "love", "love", "love", "love", "wangxiaona"]
c = Counter(s)
print(c)

