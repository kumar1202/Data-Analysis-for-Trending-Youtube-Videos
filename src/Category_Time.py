import pandas as pd
from datetime import datetime as dt
from matplotlib import pyplot as plt
from matplotlib import dates as mdt
import collections as cl

csv = pd.read_csv('../datasets/DEvideos.csv')

df = pd.DataFrame(csv)

# print(df.head())
type = list(df.category_id)
time = [x[0:10] for x in list(df.trending_date)]
sz = len(type)
cnt = cl.OrderedDict()
for i in range(sz):
    a = dt.strptime('20' + time[i], '%Y.%d.%m').date()
    b = type[i]
    if a not in cnt:
        cnt[a] = [0]*50
        cnt[a][b] = 1
    else:
        cnt[a][b] += 1

xs = [d for d in list(cnt.keys())]

ys = [x[1] for x in list(cnt.values())]

plt.plot(xs, ys)
plt.gcf().autofmt_xdate()
plt.show()



