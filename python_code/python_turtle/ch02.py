import numpy as np
z= 'link_to_iris'
print(z.capitalize())

x=np.array([10, 15, 22, 13, 17, 20, 8])
x_small = x[x >= 15]
print(np.std(x))

x = np.array([9, 6, 3])
for j in x:
    print(str(j) + ' ')

import pandas as pd
iris = pd.read_csv('link_to_iris', chunksize = 4)
next(iris)
print(next(iris))

#                eggs  salt  spam
# month country
# feb   spain     110  50.0    31
# jan   ireland    47  12.0    17
# mar   france    221  89.0    72

df = pd.DataFrame({"month": ['feb', 'jan', 'mar'],"country": ['spain', 'ireland', 'france'],"eggs": [110, 47, 211], "salt": [4, 5, 6],})
df_idx=df.set_index(['month','country'])
print(df_idx)
df_rev=df_idx.unstack()
print(df_rev)


df1 = pd.DataFrame({"month": ['feb', 'jan', 'mar'],"country": ['spain', 'ireland', 'france'],"eggs": [1, 2, 3], "salt": [4, 5, 6]})
df2 = pd.DataFrame({"month": ['feb', 'jan', 'mar'],"country": ['spain', 'ireland', 'france'],"eggs": [22, 34, 89], "salt": [123, 234,784]})
d={'one': df1, 'two': df2}
print(type(d))
x=pd.concat(d)
print(x)
# You have the following DataFrame df:
#
#               eggs  salt  spam
# apr portugal    44    18     5
#     usa         36    95    63
# feb france      93    56    10
#     spain       67    20    88
# jan england     90    33    93
#     ireland     62    21    94
# jun germany     96    75    79
#     italy       52    99     7
# mar china       83    43    19
#     india        5     6    98