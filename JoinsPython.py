import pandas as pd 

df1 = pd.read_csv('/Users/vishal/Documents/pythoncode2023/person.txt' , sep = '|')
df2 = pd.read_csv('/Users/vishal/Documents/pythoncode2023/personemail.txt' , sep = '|')

# sep = '\t'

ddff = df2.loc[:,"BusinessEntityID"]

print(ddff)
print(df2)

# print(df1[BusinessEntityID])

print("ji")
print('hi')



