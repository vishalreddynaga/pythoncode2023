import pandas as pd 

list =[]
string = " "
i = 0

ListOne = {'KeyListOne' : ["LegMRN|FirstName|LastName" , "123|john|smith" , "456|Rock|R"]}

df = pd.DataFrame(ListOne)
for index, row in df.iterrows():
    list.append(row['KeyListOne'])

for x in list:
#   i = i + 1
  string = x 
  split = x.split("|")
#   print(split[0] + "|" + split[1])
  if split[1] == 'john':
     i = i + 1
     print(string + "|" + split[0])
