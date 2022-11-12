import pymysql
from pylab import *
from matplotlib import *
db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='20030729a', database='movie')
cursor = db.cursor()
sql = "select count(*) cnt,Director from movie.movie_data group by Director order by cnt desc;"
i = 0
x = list()
y = list()
name = list()
cursor.execute(sql)
res1 = cursor.fetchall()

for row in res1:
    print(row)
    # i += 1
    # x.append(i)
    # y.append(row[0])
    # a = str(row[1])
    # name.append(a)
# matplotlib.pyplot.yticks(name)
# x = [1,2,3,4,5,6]
# y = [3,5,1,7,9,12]
#x指定其实位置从0开始，bottom指定水平条其实位置为左侧，height指定绘图的水平条的宽度，width指定绘制的水平条的长度，orientation指定要绘制的是水平条，color指定颜色
bar(x=0,bottom=y,height=1,width=y,orientation='horizontal',color='red')
show()