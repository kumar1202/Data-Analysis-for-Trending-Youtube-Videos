# Data-Analysis-of-Trending-Youtube-Videos
Project for ECE 143 Fall 2018  
Group 13: [Jialun Lyu](https://github.com/pian13131), [Lin-Ying Cheng](https://github.com/lychengr3x), [Weihua Huang](https://github.com/andrewhuang51), [Yiwei Zhang](https://github.com/einiemand)

## Dataset
**Trending YouTube Video Statistics**: [https://www.kaggle.com/datasnaek/youtube-new/home](https://www.kaggle.com/datasnaek/youtube-new/home)
* The entire dataset contains 5 `csv` files and 5 `json` files(for 5 different countries), including various kind of information like video titles, channels, video categories, publish time, number of views, number of likes and dislikes, etc.

## Proposal
### Problem:
Analyze the trending videos information from the YouTube

### Motivation:
Nowadays, an increasing number of people post their videos on YouTube, and it is interesting to know whether a video is popular is dependent on its category and the cultural background of viewers. We plan to use the acquired dataset to analyze the composition and popularity associated with different factors of online videos on YouTube. We’d like to dig in deeper to elaborate the relationship between them. To be more specific, some videos are highly controversial because of its content or types. Also, we want to show how the cultural divergence affects people’s likes and the overall most popular video types to shed light on how YouTubers are supposed to refine their videos to get more subscribers, and recommend popular channels of particular video genres.

### Plan :
Firstly, we count the number of trending videos of different types at different times, with which we can see the fluctuation. We also plan to show the popularity of particular video types by examining the total views of different video types. Then, we evaluate how these attributes are associated with cultures in different countries. Finally, we calculate the ratio of likes to dislikes for every channel to show the viewers’ attitudes towards them.

## Visualization:
Please see file `Data-Analysis-of-Trending-Youtube-Videos.ipynb` [here](https://github.com/pian13131/Data-Analysis-for-Trending-Youtube-Videos/blob/master/src/Data-Analysis-of-Trending-Youtube-Videos.ipynb).


## Packages:
### 1. seaborn
* Official website [here](https://seaborn.pydata.org/examples/index.html)
* Installation:
```
# for python 2.x
pip install seaborn

# for python 3.x
pip3 install seaborn
```

### 2. numpy
* Official website [here](http://www.numpy.org/)
* Installation:
```
# for python 2.x
pip install numpy

# for python 3.x
pip3 install numpy
```

### 3. pandas
* Official website [here](https://pandas.pydata.org/)
* Installation:
```
# for python 2.x
pip install pandas

# for python 3.x
pip3 install pandas
```

## Modules:
1. [`pyplot`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html) from [`matplotlib`](https://matplotlib.org/)
2. [`json`](https://docs.python.org/3.6/library/json.html)