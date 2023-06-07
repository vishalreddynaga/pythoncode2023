import pandas as pd 

lone = []

listonefile =[]
listtwofile = []

string = " "
stringtwo = " "


ListOne = {
'KeyListOne' :
[
'LegMRN|LastName|FirstName',
'123|john|smith',
'456|Rock|R',
'789|Brock|L' ,
'111|Vishal|R' ,
'222|Raj|S'
]
}

ListTwo = {
'KeyListTwo' : 
[
'EpicMRN|LegMRN|LastName|FirstName|MultiEpic' ,
'0456|4456|Rock|R|768,4566,879' ,
'0789|789|Brock|L|8789,345' 
]
}

df = pd.DataFrame(ListOne)
for index, row in df.iterrows():
    listonefile.append(row['KeyListOne'])

dftwo = pd.DataFrame(ListTwo)
for indextwo, rowtwo in dftwo.iterrows():
	listtwofile.append(rowtwo['KeyListTwo']) 

for x in listonefile:
  string = x 
  split = x.split("|")
  lone.append(split[0])


for xtwo in listtwofile:
  listinside =[]
  stringtwo = xtwo 
  splittwo = xtwo.split("|")
  listinside.append(splittwo[1])

  InSideList = splittwo[4]

  InSideSplit = len(InSideList.split(",")) > 1
  InSideSplitTwo = InSideList.split(",")
  if InSideSplit == True:
    for GetInSideSplitTwo in InSideSplitTwo:
        listinside.append(GetInSideSplitTwo)

       
    set1 = set(lone)
    set2 = set(listinside)

    if set1.intersection(set2):
        print(stringtwo)
    else:
        pass
        

        

