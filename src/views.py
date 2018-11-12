import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from category import *


# read csv file
df = pd.read_csv(csv_at('ca'))

# get specific column
v_df = df[['category_id', 'views']]
# print(f"\nv_df: \n{v_df.head(20)}\n")

# Combine rows with same category_id
V_DF = v_df.groupby('category_id')['views'].sum().rename('total_views').\
    reset_index().sort_values(by='total_views', ascending=False)
# print(f"\nV_DF: \n{V_DF}\n")

# new column of dataframe: category_name
V_DF['category_name'] = V_DF.category_id.map(lambda x: category_name(x))
# print(V_DF)

# plot figure
fig = V_DF.plot.bar(x='category_name', y='total_views', rot=45, legend=None)
fig.set_xlabel('Categories')
fig.set_ylabel('Views in Canada')
plt.show()
plt.close()