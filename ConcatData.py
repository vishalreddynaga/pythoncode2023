with open(r"/Users/vishal/Documents/pythoncode2023/ConcatDatatext.txt") as ReadFile:
    ReadLines = ReadFile.readlines()
    for ReadLineByLine in ReadLines:
        Split = ReadLineByLine.split("|")
        # print(Split[0])
        fname = Split[0]
        # print(len(fname))

        if len(fname) == 3:
            print("0" + fname)
        else:
            print(fname)

    
