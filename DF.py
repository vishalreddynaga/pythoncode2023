Map = {}

lst =['MRN|Lname|Fname|Path|EpicMRN\n', 
    '123|John|Smith|path|321\n', 
    '452|Rock|R|path|254\n']

for FileReadENCLineByLine in lst:
        SplitENC = FileReadENCLineByLine.split("|")
        Map.update({SplitENC[0] : FileReadENCLineByLine})
        print(SplitENC[0] + "|" + FileReadENCLineByLine)
