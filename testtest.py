# import os

# path = "/Users/vishal/Documents/test"

# os.chdir(path)


# def read_text_file(file_path):
#     with open(file_path, 'r') as f:
#         print(f.read())


# for file in os.listdir():
#     if file.endswith(".txt"):
#         file_path = f'{path}/{file}'

#         read_text_file(file_path)

import os
# find all the txt files in the dataset folder
inputs = []
for file in os.listdir("/Users/vishal/Documents/test"):
    if file.endswith(".txt"):
        inputs.append(os.path.join("/Users/vishal/Documents/test", file))

# concatanate all txt files in a file called merged_file.txt
with open("/Users/vishal/Documents/test/merged_file.txt", 'w') as outfile:
    for fname in inputs:
        with open(fname, encoding="utf-8", errors='ignore') as infile:
            outfile.write(infile.read())