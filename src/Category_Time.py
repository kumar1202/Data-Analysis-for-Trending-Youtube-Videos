import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

csv = pd.read_csv('../datasets/DEvideos.csv')
df_DE = pd.DataFrame(csv)
csv = pd.read_csv('../datasets/CAvideos.csv')
df_CA = pd.DataFrame(csv)
csv = pd.read_csv('../datasets/FRvideos.csv')
df_FR = pd.DataFrame(csv)
csv = pd.read_csv('../datasets/GBvideos.csv')
df_GB = pd.DataFrame(csv)
csv = pd.read_csv('../datasets/USvideos.csv')
df_US = pd.DataFrame(csv)

p_time = [int(x[11:13]) for x in list(df_DE.publish_time)]
mp_DE = [0]*24
for i in p_time:
    mp_DE[i]+=1

p_time = [int(x[11:13]) for x in list(df_CA.publish_time)]
mp_CA = [0] * 24
for i in p_time:
    mp_CA[i] += 1

p_time = [int(x[11:13]) for x in list(df_FR.publish_time)]
mp_FR = [0] * 24
for i in p_time:
    mp_FR[i] += 1

p_time = [int(x[11:13]) for x in list(df_GB.publish_time)]
mp_GB = [0] * 24
for i in p_time:
    mp_GB[i] += 1

p_time = [int(x[11:13]) for x in list(df_US.publish_time)]
mp_US = [0] * 24
for i in p_time:
    mp_US[i] += 1

dic = {'DE':mp_DE,'CA':mp_CA,'FR':mp_FR,'GB':mp_GB,'US':mp_US}
frame = pd.DataFrame(dic)

sns.lineplot(data=frame, palette="tab10", linewidth=1.5)

plt.show()

