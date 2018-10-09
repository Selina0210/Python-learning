#1----
#导入模块，需要模块名作为前缀
import m1
#利用模块里的类实例化对象
s=m1.student('selina',18)
s.say()
#调用模块里的函数
m1.hello()

#2---
#导入模块里的特定函数，不用带模块名
from m1 import hello
hello()
#导入模块里的特定类
from m1 import student
s1=student('lili',20)
s1.say()