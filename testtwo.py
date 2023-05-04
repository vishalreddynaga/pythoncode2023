# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 400, 900]
# }

# #load data into a DataFrame object:
# df = pd.DataFrame(data)

# print(df) 



import pandas as pd
   

def testt():
  print("testtCute")


lists = []  
mystring = " "


d = {'col1':["DMD|smith","DYSF|john", "hbibg|bib"], 'col2':[33,44,66]}
df = pd.DataFrame(d)
for index, row in df.iterrows():  
  # print(row['col1'])
  lists.append(row['col1'])
  # print(index)



for x in lists:
  mystring += ' ' + x+ "\n"
print(mystring)

# FileRead = mystring.split("|")



