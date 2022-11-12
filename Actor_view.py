import pymysql
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator


# 从数据库中获取数据阶段
db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='20030729a', database='movie')
cursor = db.cursor()
sql = "select count(*) cnt,Actor,avg(Score) from movie.movie_data group by Actor order by avg(Score) desc;"

cursor.execute(sql)
res1 = cursor.fetchall()

name = list()
cnt = list()
count = list()
Score = list()
i = 0
for row in res1:
    i += 1
    count.append(i)
    name.append(row[1])
    cnt.append(row[0])
    Score.append(row[2])

# 画图像阶段

plt.rcParams['font.family'] = 'SimHei'
# 建立图标
fig = plt.figure(num=1, figsize=(100, 100), dpi=45)

# 设置坐标轴阶段

# 设置坐标轴的范围
plt.xlim((0, 100))
plt.ylim((0, 70))

# 隐藏无用轴
ax = plt.gca()

# 将上边的坐标轴颜色设置为空，不显示
ax.spines['top'].set_color('none')

# 将x轴设置为底部bottom,将y轴设置为顶部top
ax.xaxis.set_ticks_position('bottom')
# ax.xaxis.set_ticks_position('left')

# 将x轴和y轴(底轴和左轴的位置设置为坐标原点)
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
# 设置坐标轴的名字
plt.xlabel('Actor', fontsize=30)
plt.ylabel('Number', fontsize=30)

x = MultipleLocator(10)    # x轴每10一个刻度
y = MultipleLocator(15)    # y轴每15一个刻度

new_ticks = np.linspace(0, 100, 100)
plt.xticks(count, name, rotation=90)
l1 = ax.plot(name, cnt, color='blue', linewidth=10.0, linestyle="-")


ax2 = ax.twinx()
# ax2.xaxis.set_ticks_position('bottom')
# ax2.xaxis.set_ticks_position('right')
plt.ylim(5,10)
l2 = ax.plot(name, Score, color='red', linewidth=10.0, linestyle='--')
ax2.set_ylabel('Score', fontsize=30)

ax2.spines['top'].set_color('none')

ax.legend(['Number', 'Score'], title='图例',)

plt.show()
