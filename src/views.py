import pandas as pd
import matplotlib.pyplot as plt
from category import *


# read csv file
df = pd.read_csv(csv_str('ca'))

# get specific column
v_df = df[['category_id', 'views']]
# print(f"\nv_df: \n{v_df.head(20)}\n")

# Combine rows with same category_id
V_DF = v_df.groupby('category_id')['views'].sum().rename('total_views').\
    reset_index().sort_values(by='total_views', ascending=False)
# print(f"\nV_DF: \n{V_DF}\n")

# Make a list of category_id from DataFrame
id_lst = V_DF.category_id.tolist()
# print(id_lst)
# print(id(id_lst))

# Convert number into name
id_lst[:] = [cat_name(i) for i in id_lst]
# print(id_lst)
# print(id(id_lst))

fig = V_DF.plot.bar(x='category_id', y='total_views', rot=45, legend=None)
fig.set_xlabel('Categories')
fig.set_ylabel('Views in Canada')
fig.set_xticklabels(id_lst)
plt.show()
plt.close()
