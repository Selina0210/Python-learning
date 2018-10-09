import shutil

# copy() 复制文件
#  格式：shutil.copy(来源路径，目标路径)
#  返回值：返回目标路径
# 拷贝的同时，可以给文件重命名
rst = shutil.copy("/Users/Administrator/图灵Python学习笔记/s1.txt","/Users/Administrator/图灵Python学习笔记/s2.txt")
print(rst)

# copy2() 复制文件，保留元数据（文件信息）
#  格式：shutil.copy2(来源路径，目标路径)
#  返回值：返回目标路径
#  注意：copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据


# copyfile()将一个文件中的内容复制到另外一个文件当中
#  格式：shutil.copyfile（'源路径','目标路径')
#  返回值：无
rst = shutil.copyfile("s3.txt", "s4.txt")
print(rst)

# move() 移动文件/文件夹
#  格式：shutil.move(源路径，目标路径)
#  返回值：目标路径！
rst  = shutil.move("/Users/Administrator/图灵Python学习笔记/selina", "/Users/Administrator/图灵Python学习笔记/s")
print(rst)

