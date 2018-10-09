# 需要单独导入
import time

# 时间模块的属性
# timezone: 当前时区和UTC时间相差的秒数，在没有夏令时的情况下的间隔,东八区的是 -28800
# altzone  获取当前时区与UTC时间相差的秒数，在有夏令时的情况下，
# daylight 测当前是否是夏令时时间状态, 0 表示是
print(time.daylight)

# 得到时间戳
time.time()

# localtime， 得到当前时间的时间结构
# 可以通过点号操作符得到相应的属性元素的内容
t = time.localtime()
print(t.tm_hour)

#asctime() 返回元组的正常字符串化之后的时间格式
# 格式：time.asctime（时间元组）
# 返回值:字符串 Tue Jun  6 11:11:00 2017
t = time.localtime()

tt = time.asctime(t)
print(type(tt))
print(tt)

# ctime: 获取字符串化的当前时间
t = time.ctime()
print(type(t))
print(t)

# mktime() 使用时间元组获取对应的时间戳
# 格式：time.mktime（时间元组）
# 返回值：浮点数时间戳

lt = time.localtime()
ts = time.mktime(lt)
print(type(ts))
print(ts)

# sleep: 使程序进入睡眠，n秒后继续

for i in range(10):
    print(i)
    time.sleep(1)


def p():
    time.sleep(2.5)


t0 = time.clock()
# p()
time.sleep(3)
t1 = time.clock()
print(t1 - t0)

# strftime:将时间元组转化为自定义的字符串格式
'''
格式  含义  备注
%a  本地（locale）简化星期名称    
%A  本地完整星期名称    
%b  本地简化月份名称    
%B  本地完整月份名称    
%c  本地相应的日期和时间表示    
%d  一个月中的第几天（01 - 31）   
%H  一天中的第几个小时（24 小时制，00 - 23）   
%I  一天中的第几个小时（12 小时制，01 - 12）   
%j  一年中的第几天（001 - 366）  
%m  月份（01 - 12） 
%M  分钟数（00 - 59）    
%p  本地 am 或者 pm 的相应符    注1
%S  秒（01 - 61）  注2
%U  一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周   注3
%w  一个星期中的第几天（0 - 6，0 是星期天） 注3
%W  和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始  
%x  本地相应日期  
%X  本地相应时间  
%y  去掉世纪的年份（00 - 99）    
%Y  完整的年份   
%z  用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）      
%%  %号本身
'''
# 把时间表示成， 2018年3月26日 21:05
t = time.localtime()
ft = time.strftime("%Y年%m月%d日 %H:%M" , t)
print(ft)

