import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from category import *


result = pd.DataFrame()
for area in AREA:
    # read csv file and get specific column
    # Combine rows with same category_id
    df = pd.DataFrame(pd.read_csv(csv_at(area))[['category_id', 'views']]).groupby('category_id')[
        'views'].sum().rename('Views in Area').reset_index()
    df['Areas'] = AREA_FULL_NAME[area]
    result = result.append(df)

# Add one new column: `Categories`
result.insert(loc=1, column='Categories',
              value=result.category_id.map(lambda x: category_name(x)))

# Add one new column `Total Views` of 5 areas.
result['Total Views'] = result.groupby(
    'category_id')['Views in Area'].transform('sum')

# Sort total views in descending order.
result = result.sort_values(
    by='Total Views', ascending=False).reset_index(drop=True).reset_index()
print(result.head(50))

# Increase font size
sns.set(font_scale = 2)
fig1, ax1 = plt.subplots()

# Plot area views at ax1.
fig_area = sns.catplot(x="Categories", y="Views in Area", data=result.head(35), hue="Areas",
                       hue_order=['Canada', 'France', 'Germany', 'Great British', 'USA'],
                       kind="bar", palette="muted", edgecolor="1", alpha=0.85, legend_out=False, ax=ax1)

# Plot total views at ax2 which is twin ax of ax1.
ax2 = ax1.twinx()
fig_total = sns.catplot(x="Categories", y="Total Views", data=result.head(35),
                        kind='point', color="b", ax=ax2)

# set figure
ax1.set_title("Views in different categories and areas", fontsize=30)
ax1.grid(None)


plt.show()