# list1 = [ "12" , "13", "14"  ]
# list2 = ["13"]


# if list2  in list1:
#     print("got")


# if "13" in list1:
#     print("got")
# print ("13" in list1)



# l1 = [10, 20, 30, 40, 50]
# l2 = [50, 10, 30, 20, 60]

# a = set(l1)
# b = set(l2)

# if a == b:
#     print("Lists l1 and l2 are equal")
# else:
#     # print("Lists l1 and l2 are not equal")
#     print(l2)

# def get_difference(list_a, list_b):
#     non_match_a  = set(list_a)-set(list_b)
#     non_match_b  = set(list_b)-set(list_a)
#     non_match = list(non_match_a) + list(non_match_b)
#     return non_match

# list_aa = []
# list_bb = []

# with open("InTest.txt") as File:
#     FileRead = File.readlines()
#     for ReadLineByLine in FileRead:
#         Split = ReadLineByLine.split("|")
       
#         list_aa.append(Split[0])
#         list_bb.append(Split[1].replace("\n" , ""))


#     non_match = get_difference(list_bb, list_aa)
#     print("Non-match elements: ", non_match)









# ---working present in list_a but not in list b 

# def non_match_elements(list_a, list_b):
#     non_match = []
#     for i in list_a:
#         if i not in list_b:
#             non_match.append(i)
#     return non_match
       

# list_a = [2, 44, 6, 8, 10, 12]
# list_b = [2, 4, 6, 8, 11, 23, 67, 22]

# non_match = non_match_elements(list_a, list_b)
# print("No match elements: ", non_match)

# -------------------------------------------------
def non_match_elements(list_a, list_b):
    non_match = []
    for i in list_a:
        if i not in list_b:
            non_match.append(i)
    return non_match



list_aa = []
list_bb = []

with open("InTest.txt") as File:
    FileRead = File.readlines()
    for ReadLineByLine in FileRead:
        Split = ReadLineByLine.split("|")
       
        list_bb.append(Split[0])
        list_aa.append(Split[1].replace("\n" , ""))

non_match = non_match_elements(list_aa, list_bb)
print("No match elements: ", non_match)