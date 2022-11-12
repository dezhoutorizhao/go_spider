import pymysql
from pylab import *
from matplotlib import *
# import xlwt
# excel = xlwt.Workbook(encoding='utf-8')
# sheet = excel.add_sheet('Mysql数据库')
# sheet.write(0,n0, 'Title')
# sheet.write(0, 1, 'id')
# sheet.write(0, 2, 'Director')
# sheet.write(0, 3, 'Actor')
# sheet.write(0, 4, 'Year')
# sheet.write(0, 5, 'Score')
# sheet.write(0, 6, 'Quote')
db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='20030729a', database='movie')
cursor = db.cursor()
sql = "select count(*) cnt,Director from movie.movie_data group by Director order by cnt desc;"
i = 0
# 可视化背景准备,创建一个100*100点大小的图，并设置分辨率为100

# figure(figsize=(8,6), dpi=80)
try:
    cursor.execute(sql)
    res1 = cursor.fetchall()

    for row in res1:
        i += 1
        print(1)
        subplot(100,100,i)
        print(2)
        bar(y=0,bottom=x,height=row[0],width=0.3)

        # Title = row[0]
        # id = row[1]
        # Director = row[2]
        # Actor = row[4]
        # Year = row[5]
        # Score = row[6]
        # Quote = row[7]
        # database = row[0]
        # table = row[1]
        # c1 = row[0]+'.'+row[1]
        # c2 = 'select count(*) from %s' % c1
#  try:
#   cursor.execute(c2)
#   res2=cursor.fetchall()
#   for num in res2:
#     count=num[0]
#     i=i+1
#     sheet.write(i,0,Title)
#     sheet.write(i,1,id)
#     sheet.write(i,2,Director)
#     sheet.write(i,2,Actor)
#     sheet.write(i,2,Year)
#     sheet.write(i,2,Score)
#     sheet.write(i,2,Quote)
#  except:
#   print('Error1,Please check your code')
except:
    print('Error2,Please check your code')
show()
# excel.save('D:\go爬虫2\mysql.xls')
db.close()
