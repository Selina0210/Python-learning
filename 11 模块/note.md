#1、模块
- 一个模块就是一个包含Python代码的文件，后缀名是.py就可以，最好以字母开头命名，数字命名易出现错误。在编写代码需要时，直接拿来用即可。
-如何使用模块
    -模块直接导入，相当于将模块内容直接复制粘贴过来，会直接全部执行一遍
        -语法：(module_name即包所存的文件名)
            import module_name  #导入包
            
            s=module_name.class_name  #实例化包里所定义类的对象
            s.function #调用类内的函数
            
            module_name.function_name  #调用包里定义的函数
            
    -import 模块 as 别名
        -导入的同时给模块起一个别名
        -其余用法同上        
    -from module_name import func_name,class_name 
        -按上述方法有选择性的导入
        -使用时可以直接使用导入的内容，不需要前缀
    -from module_name import *
        -将模块中所有内容导入，可以不用加包名前缀     
- 'if __name__ == '__main__''
    -可以避免模块被导入时代码被动执行
    -建议每个程序以此句开始，作为程序入口
#2、模块的搜索路径和存储
- 搜索路径
    -import sys
     print（sys.path） 获取路径列表
-添加搜索路径
    sys.path.append(dir)
-模块的加载顺序
    1、搜索内存中已经加载好的模块
    2、搜索Python的内置模块
    3、搜索sys.path路径


            


    
    
