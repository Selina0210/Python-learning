#1.导入包，可直接使用__init__.py中的内容，调用__init__.py里的inInit()函数
import pkg01
pkg01.inInit()

#2.导入包内的模块
import pkg01.mdl01
pkg01.mdl01.hello()  #调用模块内的hello函数
s=pkg01.mdl01.student('selina',18) #使用模块内的类对对象进行实例化
s.say() #调用类中的函数
