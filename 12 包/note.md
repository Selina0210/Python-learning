#3、包
-包是一种组织管理代码的方式，包里面存放的是模块
-用于把模块包含在一起的文件夹称为包
-自定义包的结构
    /---包
    /---/--- __init__.py  包的标志文件
    /---/--- 模块1
    /---/--- 模块2
    /---/--- 模块n
    /---/--- 子包（子文件夹）
    /---/---/--- __init__.py 包的标志文件
    /---/---/--- 子包模块1
    /---/---/--- 子包模块2
    /---/---/--- 子包模块n
-包的导入操作
    - import package_name
        -直接导入一个包，可以使用__init__.py中的内容
        -使用方式：
            package_name.func_name
            package_name.class_name
    - import package_name as 别名
        -具体用法与上述相同
        -注意：默认导入__init__.py的内容
    - import package.module
        -导入包里某一个具体的模块
        -使用方法：
            package.module.func_name
            package.module.class.func_name
            package.module.class.var
    - import package.module as 别名
        -与上述相同
    - from...import
        -from package import module1,module2,module3...
            -此种导入方法不执行__init__.py的内容
            -使用方法：
            from pkg01 import mdl01
            mdl01.hello()
        - from package import * 
            -只导入当前包__init__.py里的所有内容
            -使用方法：
                func_name()
                class_name.func_name()
                class_name.var
        - from package.module import *
            -导入包中指定模块的所有内容
            -使用方法：
                func_name()
                class_name.func_name()
    -在开发环境中经常会使用其他模块，可以在当前包中直接导入其他模块的内容
        - import 完整的包或者模块的路径
    - '__all__'的用法
        -在使用from package.module import *的时候，*可以导入的内容  
        -__init__.py中为空，或者没有__all__的话，那么只把__init__.py中的导入
        -__init__.py如果设置了__all__的值，那么只按照__all__指定的子包或者模块进行导入，不会再载入__init__.py的其他内容
        - __all__=[ 'module1','module2','module3'...]    
           
# 命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
-作用：防止命名冲突
    setname()
    student.setname()    
              
    