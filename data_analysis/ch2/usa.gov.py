#!/usr/bin/env python3
# --coding:utf8---

import json
from collections import defaultdict as dd
from collections import Counter
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

path = 'd:\\pycharm_data\\data_analysis\\ch2\\example.txt'
records = [json.loads(line) for line in open(path)]
# print(records[0])
# print(len(records))
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
#print(time_zones)

def get_counts(seq):
    counts = {}
    for x in seq:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
count1 = get_counts(time_zones)
#print(count1)
def get_count2(seq):
    counts = dd(int)
    for x in seq:
        counts[x] += 1
    return counts
count2 = get_count2(time_zones)
print(count2)

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

#print(top_counts(count1))
counts = Counter(time_zones)
#print(counts.most_common(10))

frame = DataFrame(records)
#print(frame)
#print(frame['tz'][:10])
tz_counts = frame['tz'].value_counts()
#print(tz_counts[:10])
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unkown'
tz_counts_clean = clean_tz.value_counts()
#print(tz_counts_clean[:10])

tz_counts_clean[:10].plot(kind='barh',rot=0)
#plt.show()

results = Series([x.split()[0] for x in frame.a.dropna()])
#print(results.value_counts()[:8])
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
#print(operating_system[:5])
by_tz_os = cframe.groupby(['tz',operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
#print(agg_counts[:10])
indexer = agg_counts.sum(1).argsort()
#print(indexer[:10])
count_subset = agg_counts.take(indexer)[-10:]
#print(count_subset)
count_subset.plot(kind='barh', stacked=True)
#plt.show()
#normed_subset = count_subset.div(count_subset.sum(1),aixs=0)
#normed_subset.plot(kind='barh', stacked=True)
#plt.show()

#################### MovieLens 1M #################
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('movieslens/users.dat', sep='::', header=None, names=unames, engine='python')
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('movieslens/ratings.dat', sep='::', header=None, names=rnames, engine='python')
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movieslens/movies.dat', sep='::', header=None, names=mnames, engine='python')
mdata = pd.merge(pd.merge(ratings, users), movies)
#print(mdata)
mean_ratings = mdata.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
mean_ratings2 = mdata.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
#print(mean_ratings[:5])
ratings_by_title = mdata.groupby('title').size()
#print(ratings_by_title[:5])
active_titles = ratings_by_title.index[ratings_by_title>=250]
#print(active_titles)
mean_ratings = mean_ratings.ix[active_titles]
#print(mean_ratings)
top_female_rating = mean_ratings.sort_values(by='F', ascending=False)
#print(top_female_rating[:10])
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
print(sorted_by_diff[::-1][:15])
ratings_std_by_title = mdata.groupby('title')['rating'].std()
ratings_std_by_title = ratings_std_by_title.ix[active_titles]
print(ratings_std_by_title.sort_values(ascending=False))
