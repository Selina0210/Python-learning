# 1、常用模块
- calendar
- time
- datetime
- timeit
- os
- shutil
- zip
- math
- string
- 上述所有模块使用理论上都应该先导入，string是特例
- calendar，time，datetime的区别参考中文意思

# 2、calendar模块
- 跟日历相关的模块


# 3、time模块
### 时间戳
    - 一个时间表示，根据不同语言，可以是整数或者浮点数
    - 是从1970年1月1日0时0分0秒到现在经历的秒数
    - 如果表示的时间是1970年以前或者太遥远的未来，可能出现异常
    - 32位操作系统能够支持到2038年

### UTC时间
    - UTC又称为世界协调时间，以英国的格林尼治天文所在地区的时间作为参考的时间，也叫做世界标准时间。
    - 中国时间是 UTC+8 东八区
  
### 夏令时
    - 夏令时就是在夏天的时候将时间调快一小时，本意是督促大家早睡早起节省蜡烛！ 每天变成25个小时，本质没变还是24小时
    
### 时间元组 
    - 一个包含时间内容的普通元组
    
    
        索引      内容    属性            值

        0       年       tm_year     2015
        1       月       tm_mon      1～12
        2       日       tm_mday     1～31
        3       时       tm_hour     0～23
        4       分       tm_min      0～59
        5       秒       tm_sec      0～61  60表示闰秒  61保留值
        6       周几     tm_wday     0～6
        7       第几天    tm_yday     1～366
        8       夏令时    tm_isdst    0，1，-1（表示夏令时）
        
# datetime.datetime 模块
- 提供比较好用的时间而已
- 类定义

       class datetime.datetime(year, month, day[, hour
                [, minute
                [, second
                [, microsecond
                [, tzinfo]]]]])
      # The year, month and day arguments are required.
      MINYEAR <= year <= MAXYEAR
      1 <= month <= 12
      1 <= day <= n
      0 <= hour < 24
      0 <= minute < 60
      0 <= second < 60
      0 <= microsecond < 10**
- 类方法

`               
datetime.today(): 返回当前本地datetime.随着 tzinfo None. datetime.fromtimestamp(time.time()).
datetime.now([tz]): 返回当前本地日期和时间, 如果可选参数tz为None或没有详细说明,这个方法会像today().
datetime.utcnow(): 返回当前的UTC日期和时间, 如果tzinfo None ,那么与now()类似.
datetime.fromtimestamp(timestamp[, tz]): 根据时间戳返回本地的日期和时间.tz指定时区.
datetime.utcfromtimestamp(timestamp): 根据时间戳返回 UTC datetime.
datetime.fromordinal(ordinal): 根据Gregorian ordinal 返回datetime.
datetime.combine(date, time): 根据date和time返回一个新的datetime.
datetime.strptime(date_string, format): 根据date_string和format返回一个datetime.

实例方法

datetime.date(): 返回相同年月日的date对象.
datetime.time(): 返回相同时分秒微秒的time对象.
datetime.replace(kw): kw in [year, month, day, hour, minute, second, microsecond, tzinfo], 与date类似.
类属性

datetime.min: datetime(MINYEAR, 1, 1).
datetime.max: datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999).

实例属性(read-only)

datetime.year: 1 至 9999
datetime.month: 1 至 12
datetime.day: 1 至 n
datetime.hour: In range(24). 0 至 23
datetime.minute: In range(60).
datetime.second: In range(60).
datetime.microsecond: In range(1000000).

# os - 操作系统相关
- 跟操作系统相关，主要是文件操作
- 于系统相关的操作，主要包含在三个模块里
    - os， 操作系统目录相关
    - os.path, 系统路径相关操作
    - shutil， 高级文件操作，目录树的操作，文件赋值，删除，移动
- 路径：
    - 绝对路径： 总是从根目录上开始
    - 相对路径： 基本以当前环境为开始的一个相对的地方