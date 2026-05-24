# print("------------------REGULAR EXPRESSION-----------------------------")
# import re
# count =0
# pattern = re.compile("function")
# matcher = pattern.finditer("A function is python is defined by def keyword . the general syntax looks like this : 'def function_name(self): ' the parameterpython list contains none or mre parameter")
# for i in matcher:
#     count +=1
#     print(i.start(),"....", i.end(),"....",i.group())
# print("the number of occurence :" , count)
# print()

# print("------------------------------------------------------")
# import re
# count =0
# matcher = re.finditer("hi","hihihihihihihihi")
# for i in matcher:
#     count +=1
#     print(i.start(),"....", i.end(),"....",i.group())
# print("the number of occurence:" , count)
# print()

# print("-----------------------------------------------------------------")
# import re 
# obj = input("enter any character")
# objmatch = re.finditer(obj , "a7b @k9z")
# # print(obj match)
# for match in objmatch:
#     print(match.start(),"....", match.end(),"....",match.group())
# print()

# print("----------------------------------------------------------------")
# import re

# a = input("Enter string to perform match operation: ")

# mtch = re.match(a, "python is very important language.")

# print(mtch)

# if mtch is not None:
#     print("Match found at the beginning:")
#     print(mtch.start(), " ", mtch.end())
# else:
#     print("There is no matching at beginning level.")

# print("------------------------------------------------------------------")
# import re

# a = input("Enter string to perform match operation: ")

# mtch = re.fullmatch(a, "pythonisvery")

# print(mtch)

# if mtch!=None:
#     print("Match found :")
#     print(mtch.start(), " ", mtch.end())
# else:
#     print("full match fnot founf.")

# print("-----------------------------------------------------------------")

# import re

# a=input("enter mail-id:")
# b = re.fullmatch("\w[a-zA-Z0-9_]*@gmail[.]com",a)
# if b!=None:
#     print("valid")
# else:
#     print("invalid")
# print()

# print("------------------------------------------------")

# import re

# a=input("enter mobileno:")
# b = re.fullmatch("[0-9]\d{9}",a)
# if b!=None:
#     print("valid")
# else:
#     print("invalid")
# print()

# print("----------------------------------------------")

# import re

# a=input("enter string to perform match operation:")
# b = re.search(a, "pyrhon sss dynamic lemmm")
# print(b)
# if b!=None:
#    print(b.start(), " ", b.end()," ", b.group())
# else:
#     print("not found")
# print()

# print("-----------------------------------------------------------")
# import re

# mtch = re.finditer('[0-9a-z]', "abcd5432hertd")

# for i in mtch:
#     print(i.group(), "found at index", i.start())

# print("-----------------------------------------------------")

# import re

# obj = re.sub('[a-z]','*','2345 ABCD hjheudd fhfyr')
# print(obj)

# print("------------------------------------------------------")

# import re
# x=re.subn('[0-7]','@','ab3gdhtj17')
# print(x)
# print("the string is :", x[0])
# print("the replacement is :", x[1])
# print()

# print("------------------------PRINT THE NUMBER IN INPUT.TXT AND OUTPUT.TXT---------------------------------")

# import re

# # Take input from user
# text = input("Enter text with mobile numbers: ")

# # Write input into file
# f = open("input.txt", "w")
# f.write(text)
# f.close()

# # Read file
# f1 = open("input.txt", "r")
# data = f1.read()

# # Find 10-digit mobile numbers
# numbers = re.findall(r"\d{10}", data)

# # Write output
# f2 = open("output.txt", "w")

# for num in numbers:
#     print(num)          # Display on screen
#     f2.write(num + "\n")

# f1.close()
# f2.close()

# print("Numbers saved in output.txt")

## example  graph
# consider this graph:
# text 
#    A------B
#    |      |
#    |      |
#    C------D 
#connections:
# * A <-> B
# * A <-> C
# * B <-> D
# * C <-> D
#Adjancy matrix representation
# |   | A  | B  | C  | D  |
# | -  | -  | -  |  - | -  |
# | A  | 0 | 1  | 1  | 0  |
# | B  | 1  | 0  | 0  | 1  |
# | C  | 1 | 0  | 0  | 1  |
# | D | 0  | 1  | 1  | 0  |

    
# class graph:
#     def __init__(self, vertices):
#         self.V = vertices

#         self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
#     def display(self):
#         for row in self.matrix:
#             print(row)
#     def add_edge(self, u, v):
#         self.matrix[u][v] = 1
#         self.matrix[v][u] = 1
# g = graph(4)
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(1,3)
# g.add_edge(2,3)
# g.display()

# print("--------------HASHING------------------------------")
# print("hashing is a techniue that is used to convert data into a fixed size that is call hashing ")
# print("they hep us to store and search data very fast ")
# print("coverting big pieces of info into small addresses")

class hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hashfunction(self, key):
        return key % self.size
    
    def insert(self, key):
        index = self.hashfunction(key)
        self.table[index].append(key)

    def display(self):
        print(self.table)

h = hashtable(10)
h.insert(15)
h.insert(25)
h.insert(35)
h.display()

