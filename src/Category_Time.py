import pandas as pd
from datetime import datetime as dt
from matplotlib import pyplot as plt
import numpy as np
import collections as cl

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

cat = list(df_DE.category_id)
time = [x[0:10] for x in list(df_DE.trending_date)]
sz = len(cat)
cnt = cl.OrderedDict()
for i in range(sz):
    a = dt.strptime('20' + time[i], '%Y.%d.%m').date()
    b = cat[i]
    if a not in cnt:
        cnt[a] = [0]*50
        cnt[a][b] = 1
    else:
        cnt[a][b] += 1

xs = [d for d in list(cnt.keys())]
for i in range(50):
    ys = [x[i] for x in list(cnt.values())]
    if sum(ys)//50 > 20:
        plt.plot(xs, ys, label = str(i))

# xs = ['201711', '201712', '201801', '201802', '201803', '201804',\
#       '201805', '201806']
# btm = np.array([0]*8)
# for i in range(50):
#     ys = np.array([x[i] for x in list(cnt.values())])
#     if sum(ys)//50 > 20:
#         plt.bar(xs, ys, bottom = btm, label = str(i))
#         btm += ys

plt.legend()
plt.gcf().autofmt_xdate()
plt.show()



