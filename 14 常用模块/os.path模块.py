import os.path as op
# abspath() 将路径转化为绝对路径
# absolute 绝对
#  格式:os.path.abspath('路径')
#  返回值：路径的绝对路径形式

# linux中
# . 点号，代表当前目录
# .. 双点，代表父目录
absp = op.abspath(".")
print(absp)

# basename() 获取路径中的文件名部分
#  格式:os.path.basename(路径)
#  返回值：文件名字符串
bn = op.basename("/Users/Administrator/图灵Python学习笔记")
print(bn)
bn = op.basename("/Users/Administrator")
print(bn)

# join() 将多个路径拼合成一个路径
#  格式：os.path.join(路径1，路径2....)
#  返回值：组合之后的新路径字符串
bd = "/Users/Administrator/图灵Python学习笔记"
fn = "s"
p = op.join(bd, fn)
print(p)

# split() 将路径切割为文件夹部分和当前文件部分
#  格式:os.path.split（路径）
#  返回值：路径和文件名组成的元组
t = op.split("/Users/Administrator/图灵Python学习笔记")
print(t)
d,p = op.split("/Users/Administrator/图灵Python学习笔记")
print(d, p)

# isdir（） 检测是否是目录
#  格式：os.path.isdir(路径)
#  返回值：布尔值
rst = op.isdir("/Users/Administrator/图灵Python学习笔记")
rst

# exists() 检测文件或者目录是否存在
#  格式：os.path.exists(路径)
#  返回值:布尔值
e = op.exists("/Users/Administrator/图灵Python学习笔记/s")
e

