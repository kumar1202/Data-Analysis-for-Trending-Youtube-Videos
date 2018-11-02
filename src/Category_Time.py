import pandas as pd
from datetime import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
csv = pd.read_csv('../datasets/DEvideos.csv')
df_DE = pd.DataFrame(csv)
# csv = pd.read_csv('../datasets/CAvideos.csv')
# df_CA = pd.DataFrame(csv)
# csv = pd.read_csv('../datasets/FRvideos.csv')
# df_FR = pd.DataFrame(csv)
# csv = pd.read_csv('../datasets/GBvideos.csv')
# df_GB = pd.DataFrame(csv)
# csv = pd.read_csv('../datasets/USvideos.csv')
# df_US = pd.DataFrame(csv)

# print(df_DE.publish_time.head())
p_date = [dt.strptime(x[0:10], '%Y-%m-%d').date() for x in list(df_DE.publish_time)]
p_time = [int(x[11:13]) for x in list(df_DE.publish_time)]

cnt_weekday = [0]*7
cnt_time = [0]*24

for i in range(len(p_date)):
    cnt_weekday[p_date[i].weekday()]+=1
    cnt_time[p_time[i]]+=1

str_weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.barplot(x = 'Weekdays', y = 'Numbers', data=cnt_weekday)
# plt.subplot(2, 1, 1)
# plt.bar(str_weekday, cnt_weekday)
# plt.subplot(2, 1, 2)
# plt.bar(range(1, 25), cnt_time)
plt.show()
# xs = [d for d in list(cnt.keys())]
# for i in range(50):
#     ys = [x[i] for x in list(cnt.values())]
#     if sum(ys)//50 > 20:
#         plt.plot(xs, ys, label = str(i))


# btm = np.array([0]*8)
# for i in range(50):
#     ys = np.array([x[i] for x in list(cnt.values())])
#     if sum(ys)//50 > 20:
#         plt.bar(xs, ys, bottom = btm, label = str(i))
#         btm += ys

# plt.legend()
# plt.gcf().autofmt_xdate()
# plt.show()



