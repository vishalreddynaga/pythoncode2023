import pandas as pd


# firstname|age
# Sally|50
# Mary|40
# John|30
#j

Map = {}

data = {
  "MRN": [1,3,4],
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}

df = pd.DataFrame(data)

for index, row in df.iterrows():

  if row["firstname"] == "Sally":
    full = str(row["firstname"])+"|"+str(row["age"])
    Key = str(row["MRN"])
    Map.update({Key , full})
      
print(Map.get(3))


