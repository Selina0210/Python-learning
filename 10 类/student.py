#定义一个类
class student():
    name=None
    age=18
    height=160
    weight=105
    def homework(self):
        print(" I'm doing my homework ")
        return None

#实例化
selina=student()
#selina.other='Piano'
print(selina.name)
print(selina.age)
print(selina.height)
selina.homework()
