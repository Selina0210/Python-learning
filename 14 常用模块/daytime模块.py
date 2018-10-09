import time
import datetime

# datetime常见属性
# datetime.date: 一个理想和的日期，提供year, month, day属性
dt = datetime.date(2018, 3,26)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)

# datetime.time: 提供一个理想和的时间， 居于哦hour， minute，sec，microsec等内容
# datetime.datetime: 提供日期跟时间的组合
# datetime.timedelta: 提供一个时间差，时间长度

# datetime.datetime
from datetime import datetime
# 常用类方法：
# today：
# now
# utcnow
# fromtimestamp： 从时间戳中返回本地时间
dt = datetime(2018, 3, 26)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))

# datetime.timedelta
# 表示一个时间间隔
from datetime import datetime, timedelta
t1 = datetime.now()
print( t1.strftime("%Y-%m-%d %H:%M:%S"))
# td表示以小时的时间长度
td = timedelta(hours=1)
# 当前时间加上时间间隔后，把得到的一个小时后的时间格式化输出
print( (t1+td).strftime("%Y-%m-%d %H:%M:%S"))


# timeit-时间测量工具
# 测量程序运行时间间隔实验
def p():
    time.sleep(3.6)
t1 = time.time()
p()
print(time.time() - t1)


import timeit
# 生成列表两种方法的比较
# 如果单纯比较生成一个列表的时间，可能很难实现
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''

# 利用timeit调用代码，执行100000次，查看运行时间
t1 = timeit.timeit(stmt="[i for i in range(1000)]", number=100000)
# 测量代码c执行100000次运行结果
t2 = timeit.timeit(stmt=c, number=100000)
print(t1)
print(t2)