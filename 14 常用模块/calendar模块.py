# 使用需要先导入
import calendar
# calendar：　获取一年的日历字符串

cal = calendar.calendar(2017)
print(cal)

# 参数
# w = 每个日期之间的间隔字符数
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数
cal = calendar.calendar(2017, l=0, c=5)
print(cal)

# isleap: 判断某一年是否闰年
calendar.isleap(2000)

# leapdays: 获取指定年份之间的闰年的个数
calendar.leapdays(2001, 2018)

# month（） 获取某个月的日历字符串
# 格式:calendar.month(年，月)
# 回值：月日历的字符串
m3 = calendar.month(2018, 3)
print(m3)

# monthrange（） 获取一个月的周几开始及总天数
# 格式：calendar.monthrange(年,月)
# 回值：元组(周几开始,总天数)
# 注意：周默认 0 -6 表示周一到周天
w,t = calendar.monthrange(2017, 3)
print(w)
print(t)

# monthcalendar() 返回一个月每天的矩阵列表
# 格式：calendar.monthcalendar(年，月)
# 回值：二级列表
# 注意：矩阵中没有天数用0表示
m = calendar.monthcalendar(2018, 3)
print(type(m))
print(m)

# prcal: print calendar 直接打印日历
#calendar.prcal(2018)
help(calendar.prcal)

# prmonth() 直接打印整个月的日历
# 格式：calendar.prmonth(年，月)
# 返回值：无
calendar.prmonth(2018, 3)

# weekday() 获取周几
# 格式:calendar.weekday(年，月，日)
# 返回值:周几对应的数字
calendar.weekday(2018, 3, 26)
