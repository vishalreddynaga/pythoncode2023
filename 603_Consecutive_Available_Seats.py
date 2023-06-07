
#    Input: 
# Cinema table:
# +---------+------+
# | seat_id | free |
# +---------+------+
# | 1       | 1    |
# | 2       | 0    |
# | 3       | 1    |
# | 4       | 1    |
# | 5       | 1    |
# +---------+------+
# Output: 
# +---------+
# | seat_id |
# +---------+
# | 3       |
# | 4       |
# | 5       |
# +---------+

import pandas as pd
FreeList = []
df = pd.DataFrame({'seat_id': [1, 2, 3 , 4 , 5], 'free': [1, 0, 1 , 1 , 1]})
for index, row in df.iterrows():
    if  row['free'] == 1:
        FreeList.append(row['seat_id'])
    else:
        FreeList = []

print(FreeList)

