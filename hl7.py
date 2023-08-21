

with open("/Users/vishal/Documents/pythoncode2023/hl7messagestext.txt") as readfile:
    readfileline = readfile.readlines()
    for readfilelinebyline in readfileline:
        # print(readfilelinebyline)
        if readfilelinebyline.startswith("MSH"):
            print("MSH")