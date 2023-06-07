# /Users/vishal/Documents/pythoncode2023/DipLinesWithOutEpicMRN.txt

Map = {}


with open(r"/Users/vishal/Documents/pythoncode2023/MissingEnc.txt") as File_EpicMapping:
    File_EpicMapping_readlines = File_EpicMapping.readlines()
    for File_EpicMapping_ReadLineByLine in File_EpicMapping_readlines:
        Split_File_EpicMapping_ReadLineByLine = File_EpicMapping_ReadLineByLine.split("|")
        LegMRN_Key = Split_File_EpicMapping_ReadLineByLine[4].replace('\n' , '')    
        EpicMRN_Value = Split_File_EpicMapping_ReadLineByLine[0]
        Map.update({LegMRN_Key : EpicMRN_Value})


with open(r'/Users/vishal/Documents/pythoncode2023/DipLinesWithOutEpicMRN.txt') as File_EmptyDipLines:
    File_EmptyDipLines_readlines = File_EmptyDipLines.readlines()
    for File_EmptyDipLines_ReadLineByLines in File_EmptyDipLines_readlines:

        Split_File_EmptyDipLines_ReadLineByLines = File_EmptyDipLines_ReadLineByLines.split('|')
        LegMRN_KeyTwo = Split_File_EmptyDipLines_ReadLineByLines[4].replace('\n' , '')  
        lname = Split_File_EmptyDipLines_ReadLineByLines[1]
        fname = Split_File_EmptyDipLines_ReadLineByLines[2]    
        print(lname +"|"+ fname +"|"+ LegMRN_KeyTwo + "|"+ Map[LegMRN_KeyTwo])



