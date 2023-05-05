
ListENC = []


with open("MissingEnc.txt") as FileENC:
    FileReadENC = FileENC.readlines()
    # print(FileReadENC)
    for FileReadENCLineByLine in FileReadENC:
        SplitENC = FileReadENCLineByLine.split("|")
        ListENC.append(SplitENC[0])

with open(r"/Users/vishal/Documents/pythoncode2023/GivenMissingEnc.txt") as FileMRN:
    FileReadMRN = FileMRN.readlines()
    for FileReadMRNLineByLine in FileReadMRN:
        SplitMRN =FileReadMRNLineByLine.split("|")
        if SplitMRN[0] not in ListENC:
            print(FileReadMRNLineByLine)
 






    
