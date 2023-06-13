import pandas as pd 
df1 = pd.DataFrame({'a': ['foo', 'bar'], 'b': [1, 2]})
df2 = pd.DataFrame({'a': ['foo', 'baz'], 'c': [3, 4]})
print(df1.merge(df2, how='inner', on='a'))
listone = []

maps = {}

df11 = pd.read_csv('/Users/vishal/Documents/pythoncode2023/person.txt'  ,  sep = '|')
df22 = pd.read_csv('/Users/vishal/Documents/pythoncode2023/personemail.txt' , sep = '|')

# BusinessEntityID_str = df1['BusinessEntityID']
# FirstName_str = df1['FirstName']

# BusinessEntityID_str_len = len(BusinessEntityID_str)

# FirstName_str_len = len(FirstName_str)
# FirstName_str_set = set(FirstName_str)jhi
df11['a']=df11['a'].map(str)
df22['a']=df22['a'].map(str)
# print(df11.merge(df22, how='left', on='a'))
df = df11.merge(df22, how='left', on='a')

# print(df['a'] , df['FirstName'] , df['EmailAddress'])
ddff = df['a'] , df['FirstName'] , df['EmailAddress']

m = maps.update({df['a']  : df['FirstName'] })
# print(ddff , header=None,index=False) 
dfff = df['a'] +"|"+ df['FirstName'] +"|"+ df['EmailAddress']

dfff.to_csv('data.csv' , header=None,index=False)

# listone.append(df['FirstName'] , df['EmailAddress'])

# print(listone)
print("hi")
# print(FirstName_str_len) 
# print(len(FirstName_str_set))





