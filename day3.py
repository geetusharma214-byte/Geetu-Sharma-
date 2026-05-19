
# maximum consecutive ones

# arr=[1,1,0,1,1,1,0,1,1,1,1]
# count=0
# max_count=0
# for i in arr:
#     if i == 1:
#         count += 1
#         if count > max_count:
#             max_count = count
#     else:
#         count = 0

# print("Maximum consecutive ones:", max_count) o/p 4

# --------------------------------------------------------------------------------------------------------------

# merge intervals
# string = "abababab"
# substring = "ab"
# count = string.count(substring)
# print("Substring count:", count)  o/p=4

# ----------------------------------------------------------------------------------------------------------------

#while loop 
# i = 1
# while i<=5:
#     print(i)
#     i+= 1

# -----------------------------------------------------------------------------------------------------------------
#function
# def hello(): #called function
#  print("hello world")
# hello()

# --------------------------------------------------------------------------------------------------------------------
##arithmetic function
# def arithmetic():
#     a = int(input("enter the value of a:"))
#     b = int(input("enter the value of b :"))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul
# print(arithmetic())  yes we can print multiple Value
# print("arithmetic =", result)

#----------------------------------------------------------------------------------------------------------------------

#how many types of argument we pass in function?
# 1.positional argument
# 2.keyword argument
# 3. default argument 
# 4. variable length argument/ variable no of argument 

#1.positional argument
# def arithmetic(a,b):
#     a = int(input("enter the value of a:"))
#     b = int(input("enter the value of b :"))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul
# result = arithmetic(5,5)
# print("arithmetic =", result)

#2.keyword arguement 
# def cridential(username,password):
#     if username == password:
#         print("login sucessfully")
#     else:
#         print("invalid")
# cridential(username="admin",password="admin")

#3.default argument
# def city(c="pune"):
#     print(c)
# city("nagpur")
# city("mumbai")
# city()
# print()

#4.variable 
# def city(name):
#     print(name)
# city("nagpur","mumbai","pune")

#--------------------------------------------------------------------------------------------------------------

#modularity approach
# import sys
# def add():
#     a = int(input("Enter a number A: "))
#     b= int(input("Enter a number B: "))
#     print(a+b)    
# def sub():
#     a = int(input("Enter a number A: "))
#     b= int(input("Enter a number B: "))
#     print(a-b)    
# def mul():
#     a = int(input("Enter a number A: "))
#     b= int(input("Enter a number B: "))
#     print(a*b)   
# def div():
#     a = int(input("Enter a number A: "))
#     b= int(input("Enter a number B: "))
#     print(a/b)
# while True:
#     print("1.addition")
#     print("2.sub")
#     print("3.divsion")
#     print("4.multiply")
#     print("5.exit")
#     choice =int(input("enter your choice:"))
#     if choice ==1:
#         add()
#     elif choice ==2:
#         sub()
#     elif choice ==3:
#         mul()
#     elif choice ==4:
#         div()
#     elif choice ==5:
#         sys.exit()

# -----------------------DSA Start -------------------------------------------------------------------------


# def findbiggestNumber(sampleArray): #===========>
#     biggestNumber = sampleArray[0]  #=================== O(1)
#     for index in range (1,len(sampleArray)): #================O(N)
#         if sampleArray[index]>biggestNumber:  #===================O(1)
#             biggestNumber = sampleArray[index]  #===================O(1)
#     print(biggestNumber) #==============================================O(1)

# sampleArray= [5,7,9,2,3,4]
# findbiggestNumber(sampleArray)

# O(1) +O(1)  +O(1)  +O(1)  +O(N) = O(N)

# print("LINEAR SEARCH")

# def linearsearch(array,target):
#     for i in range (0, len(array)):
#         if array[i]== target:
#             return i
#     return -1
        
# array =[1,2,3,4,6,7,9]
# target = 7
# result =linearsearch(array,target)
# if result == -1:
#     print("target value not ofund:")
# else:
#     print("element found at index ", result)

#----------------------------------------------------------------------------------------------------------------
# removing space from the string 
#1. rstrip()
# city = input ("enter yur city name :")
# if scity == 'hyderabad ':
#     print("hello hyderabad1.Adab")
# elif == 'chennai':
#     print("hello chennai")
# elif scity== 'banglore':
#     print("banglore")
# else:
#     print("your entered city is invalid")

#--------------------------------------------------------------------------------------------------------------------
# mylist = [
#     [100, 198, 333, 323],
#     [122, 232, 221, 111],
#     [223, 565, 245, 764]
# ]
# newlist = []
# for i in range(3):
#     j=0
#     max =mylist[i][j]
#     for j in range(4):
#         c_max =mylist[i][j]
#         if max <c_max:
#             max = c_max
#     newlist.append(max)
# print(newlist)

#-------------------------------------------------------------------------------------------------------------------

# name ='geetu*is*g*good*girl'
# newname=''
# val=''
# for i in name:
#     if i !='*':
#         newname +=i
#     else:
#         val +=i
# print(newname)
# print(str(val+newname))

#--------------------------------------------------------------------------------------------------------------------
# s = "aaabbbbccceeeee"
# result = ""
# count = 1
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count += 1
#     else:
#         result += s[i - 1] + str(count)
#         count = 1
# # add last character group
# result += s[-1] + str(count)
# print(result)
#--------------------------------------------------------------------------------------------------------------------