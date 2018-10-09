# make_archive() 归档操作
#  格式:shutil.make_archive('归档之后的目录和文件名','后缀','需要归档的文件夹')
#  返回值：归档之后的地址
#help(shutil.make_archive)
# 是想得到一个叫做tuling.zip的归档文件
rst = shutil.make_archive("/Users/Administrator/图灵Python学习笔记/gwy", "zip", "/Users/Administrator/图灵Python学习笔记/g")
print(rst)


#压缩
import zipfile
#zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
# 创建一个ZipFile对象，表示一个zip文件。参数file表示文件的路径或类文件对象(file-like object)；参数mode指示打开zip文件的模式，默认值为’r’，表示读已经存在的zip文件，也可以为’w’或’a’，’w’表示新建一个zip文档或覆盖一个已经存在的zip文档，’a’表示将数据附加到一个现存的zip文档中。参数compression表示在写zip文档时使用的压缩方法，它的值可以是zipfile. ZIP_STORED 或zipfile. ZIP_DEFLATED。如果要操作的zip文件大小超过2G，应该将allowZip64设置为True。
zf = zipfile.ZipFile("/Users/Administrator/图灵Python学习笔记/gwy.zip")


# ZipFile.getinfo(name):
#  获取zip文档内指定文件的信息。返回一个zipfile.ZipInfo对象，它包括文件的详细信息。将在下面 具体介绍该对象。
rst = zf.getinfo("1.txt")
print(rst)

# ZipFile.namelist()
#  获取zip文档内所有文件的名称列表。
nl = zf.namelist()
print(nl)

# ZipFile.extractall([path[, members[, pwd]]])
#  解压zip文档中的所有文件到当前目录。参数members的默认值为zip文档内的所有文件名称列表，也可以自己设置，选择要解压的文件名称。
rst = zf.extractall("/Users/Administrator/图灵Python学习笔记/gwy")

