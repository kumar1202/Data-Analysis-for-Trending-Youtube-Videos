import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from category import *

result_view = pd.DataFrame()
for area in AREA:
    # Load csv file
    df_csv = pd.DataFrame(pd.read_csv(csv_at(area)))

    #######################################
    ### publish time in different areas ###
    #######################################
    p_time = [int(x[11:13]) for x in list(df_csv.publish_time)]
    mp_area = [0]*24
    for i in p_time:
        mp_area[i] += 1
    plt.plot(range(1, 25), mp_area, label=full_name(area))

    ################################
    ### views in different areas ###
    ################################
    df_view = df_csv[['category_id', 'views']].groupby('category_id')[
        'views'].sum().rename('Views in Area').reset_index()
    df_view['Areas'] = full_name(area)
    result_view = result_view.append(df_view)

############################################
### Plot publish time in different areas ###
############################################
plt.xticks(np.arange(1, 25))
plt.yticks(np.arange(0, 7600, 500))
plt.xlabel('Time(hour)')
plt.ylabel('Published Videos')
plt.legend(loc='upper left')


#####################################
### Plot views in different areas ###
#####################################
# Add one new column: `Categories`
result_view.insert(loc=1, column='Categories',
                value=result_view.category_id.map(lambda x: category_name(x)))

# Add one new column `Total Views` of 5 areas.
result_view['Total Views'] = result_view.groupby(
    'category_id')['Views in Area'].transform('sum')

# Sort total views in descending order.
result_view = result_view.sort_values(
    by='Total Views', ascending=False).reset_index(drop=True).reset_index()

# Increase font scale.
sns.set(font_scale=2)
sbplt_fig_view, sbplt_ax_view = plt.subplots()

# Plot area views at sbplt_ax_view.
fig_view1 = sns.catplot(x="Categories", y="Views in Area", data=result_view.head(35), hue="Areas",
                        hue_order=['Canada', 'France',
                                   'Germany', 'Great British', 'USA'],
                        kind="bar", palette="muted", edgecolor="1", alpha=0.85, legend_out=False, ax=sbplt_ax_view)

# Plot total views at sbplt_ax_view2 which is twin ax of sbplt_ax_view.
sbplt_ax_view2 = sbplt_ax_view.twinx()
fig_view2 = sns.catplot(x="Categories", y="Total Views", data=result_view.head(35),
                        kind='point', color="b", ax=sbplt_ax_view2)

# Set figure
sbplt_ax_view.set_title("Views in different categories and areas", fontsize=30)
sbplt_ax_view.grid(None)
plt.show()