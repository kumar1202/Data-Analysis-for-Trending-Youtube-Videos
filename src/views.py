import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from category import *


result = pd.DataFrame()
for area in AREA:
    # read csv file
    df = pd.read_csv(csv_at(area))

    # get specific column
    v_df = pd.DataFrame(df[['category_id', 'views']])

    # Combine rows with same category_id
    v_df = v_df.groupby('category_id')['views'].sum().rename('area_views').\
        reset_index().sort_values(by='area_views', ascending=False)
    v_df['area'] = AREA_FULL_NAME[area]
    result = result.append(v_df)

# Add one new column: `category_name`
result.insert(loc=1, column='category_name',
              value=result.category_id.map(lambda x: category_name(x)))

# Add one new column `total_views` of 5 areas.
result['total_views'] = result.groupby(
    'category_id')['area_views'].transform('sum')

# Sort total views in descending order.
result = result.sort_values(by='total_views', ascending=False).reset_index(drop=True).\
    reset_index().rename(index=str, columns={
        'category_name': 'Categories', 'area_views': 'Views in Area', 'total_views': 'Total Views', 'area': 'Areas'})

# Plot total views.
fig_total = sns.catplot(x="Categories", y="Total Views",
                        data=result.head(50), kind='point')

# Plot area views.
fig_area = sns.catplot(x="Categories", y="Views in Area", hue="Areas",
                       data=result.head(50), kind="bar", palette="muted", legend=False, ax=fig_total.ax.twinx())

plt.show()
