import pandas as pd
import collections as cl
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
p_time = [int(x[11:13]) for x in list(df_DE.publish_time)]
mp = [0]*24
for i in p_time:
    mp[i]+=1
plt.plot(range(1,25),mp, color = '#539caf', label='DE')
plt.legend(loc='upper left')
plt.show()

