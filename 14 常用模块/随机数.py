import random

# random() 获取0-1之间的随机小数
#  格式：random.random()
#  返回值：随机0-1之间的小数
print(random.random())

# 作业： 利用random函数，注意是函数，生成0-100之间的整数
a=int(random.random()*100)
print(a)

# choice() 随机返回序列中的某个值
#  格式：random.choice(序列)
#  返回值：序列中的某个值
l = [str(i)+"haha" for i in range(10)]
print(l)
rst = random.choice(l)
print(rst)

# shuffle() 随机打乱列表
#  格式：random.shuffle(列表)
#  返回值：打乱顺序之后的列表
l1 = [i for i in range(10)]
print(l1)
random.shuffle(l1)
print(l1)

# randint(a,b): 返回一个a到b之间的随机整数，包含a和b
print(random.randint(0,100))
