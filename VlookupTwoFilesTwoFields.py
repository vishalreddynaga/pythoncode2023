
ListENC = []
ListMRN = []

with open("MissingEnc.txt") as FileENC:
    FileReadENC = FileENC.readlines()
    for FileReadENCLineByLine in FileReadENC:
        SplitENC = FileReadENCLineByLine.split("|")
        # print(FileReadENCLineByLine)
        # print(SplitENC[0])
        ListENC.append(SplitENC[0])

with open(r"/Users/vishal/Documents/pythoncode2023/GivenMissingEnc.txt") as FileMRN:
    FileReadMRN = FileMRN.readlines()
    for FileReadMRNLineByLine in FileReadMRN:
        SplitMRN =FileReadMRNLineByLine.split("|")
        # print(SplitMRN[0])
        ListMRN.append(SplitMRN[0])

        if ListENC == ListMRN:
            print(FileReadMRNLineByLine)
 






    
