
#The garments company Apparel wishes to open outlets at various locations. 
# The company shortlisted several plots in these locations and wishes to select only plots that are square-shaped.
# Write an algorithm to help Apparel find the number of plots that it can select for its outlets.
# Input
# The first line of the input consists of an integer numfMots, representing the number of plots 
# shorilisted by the company for outlets (N).
# The second line consists of space-separated integers - areal, areal,,areaN 
# representing the area of theN plots selected for outlets, prepare a code for this question in python in easy way
#input: 
# 8 
# 79 77 54 81 48 34 25 16
# output:
# 3

#-------------------------------------------------------------------------------------------------------------------------

# n = int(input())
# areas = list(map(int, input().split()))
# count = 0
# for i in areas:
#     root = int(i ** 0.5)
#     if root * root == i:
#         count += 1
# print(count)

#---------------------------------------------------------------------------------------------------------------

# def func(value, values):
#     var = 1
#     values[0] = 44
# t=3
# v=[1,2,3]
# func(t,v)
# print(t,v[0])

#--------------------------------------------------------------------------------------------------

# def f(i, values = []):
#     values.append(i)
#     print(values) #return value
# f(1)  #calling function
# f(2)
# f(3)  o/p [1]
        # [1, 2]
            # [1, 2, 3]

#----------------------------------------------------------------------------------------------------------
#--------QUEUE------------------------------------------

# import sys
# from day5 import fruit

# class queue:
#     def __init__(self, size):
#         self.myqueue = []
#         self.euesize = size

#     def isFull(self):
#         if len(self.myqueue) == self.euesize:
#             return True
#         else:
#             return False

#     def enqueue(self, value):
#         if self.isFull():
#             print("Queue is full")
#         else:
#             self.myqueue.append(value)

#     def display(self):
#         print(self.myqueue)

#     def isempty(self):
#         if self.myqueue == []:
#             return True
#         else:
#             return False

#     def dequeue(self):
#         if self.isempty():
#             print("Queue is empty")
#         else:
#             self.myqueue.pop(0)

#     def peek(self):
#         if self.isempty():
#             print("Queue is empty")
#         else:
#             print(self.myqueue[0])

#     def deletequeue(self):
#         self.myqueue = None


# size = int(input("Enter the size of queue: "))
# obj = queue(size)

# print("Queue has created")

# while True:
#     print("\n1. Enqueue operation")
#     print("2. Display queue")
#     print("3. Delete operation")
#     print("4. Peek")
#     print("5. Delete queue")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         value = int(input("Enter element to add in queue: "))
#         obj.enqueue(value)

#     elif choice == 2:
#         obj.display()

#     elif choice == 3:
#         obj.dequeue()

#     elif choice == 4:
#         obj.peek()

#     elif choice == 5:
#         obj.deletequeue()
#         print("Queue deleted")

#     elif choice == 6:
#         sys.exit()

#     else:
#         print("Invalid choice")

#---------------------STACK-----------------------------------
#STACK USING LIST 
    #EASY TO IMPLEMENT 
    #SPPED PROBLEM WHEN IT GROWS
#STACK USING LIKED LIST 
    # FAST PERFORMANCE 
    # IMPLEMEMTATION IS NOT EASY 

#QUEUE USINGLIST 
# EASY TO IMPLEMENT 
#SPEED PROBLEM WHEN IT GROWS

#QUEUE USING LLINKED LIST
  # FAST PERFORMANCE 
    # IMPLEMEMTATION IS NOT EASY 

# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] +=1
#     else:
#         fruit[index] =1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))

#------------------------------------------------------------------------------------------------------------

#wAP to accept student marks and name from the keyboard and create a dictionary .
#also display student marks by taking student name

# WAP to accept student names and marks
# and create a dictionary using mydict

# mydict = {}

# n = int(input("Enter number of students: "))

# for i in range(n):
#     name = input("Enter student name: ")
#     marks = int(input("Enter student marks: "))

#     mydict[name] = marks

# while True:
#     name=input("enter student name to get marks :")
#     marks=mydict.get(name, -1)
#     if marks== -1:
#         print("student not found")
#     else:
#         print("the marks of",name, "are", marks)
#     option=input("do you want to find another student marks [yes/no]")
#     if option=="no":
#         break
# print("thanks for using our application")

#------------------------------------------------------------------------------------------------------------
#WAP to access each character of string in forward and backward direcion by using while loop?
#i/p ="learning python is very easy"

# WAP to access each character of string
# in forward and backward direction using while loop

# s = "learning python is very easy"

# n = len(s)

# i = 0

# print("Forward Direction:")

# while i < n:
#     print(s[i], end=" ")
#     i += 1


# print("\n\nBackward Direction:")

# i = -1

# while i >= -n:
#     print(s[i], end=" ")
#     i -= 1

#----------------------------------------------------------------------------------------------------------------------

#A company provides network encryption for secure data transfer.
#  The data string is encrypted prior to transmission and gets decrypted at the receiving end. 
# But due to some technical error, one encrypted data is lost and the received string is different 
# from the original string by 1 character. Now, a network administrator is tasked with finding the 
# character that got lost in the network so that he can resend that missing data.

# Write an algorithm to help Arnold find the character that was missing at the 
# receiving end present at the sending end. 

# stringSent = input("Enter sent string: ")
# stringRec = input("Enter received string: ")

# for ch in stringSent:
#     if stringSent.count(ch) != stringRec.count(ch):
#         print("Missing character is:", ch)
#         break

#----------------------------------------------------------------------------------------------------------------------------

# v=['a','e','i','o','u']
# w=input("enter the word where we will search the vowels: ")
# found=[]
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('found vowels=',found)
# print('unique vowels', len(found), 'from the given word=',w)

#----------------------------------------------------------------------------------------------------------------

#Q- A company wishes to provide cab service for their N employees. The distance of the company from each employee’s 
# residence is calculated. The distance from an employee’s residence to the company on the left side of the company 
# is represented with a negative sign, while the distance on the right side is represented with a positive sign. 
# The company wishes to find the distance for the employees who live within a particular distance range.
#Write an algorithm to find the distance for the employees who live within the distance range.


# x, y, z = map(int, input().split())

# mylist = list(map(int, input().split()))

# for j in mylist:
#     if j >= y and j <= z:
#         print(j, end=" ")

#--------------------------------------------------------------------------------------------------------------------

#   DATETIME FORMAT

# import datetime
# date = datetime.datetime.now()
# print("its now: {:%d/%m/%Y %H:%M:%S}", format(date))

#----------------------------------------------------------------------------------------------------------------

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)       o/p= true false true

#-------------------------------------------------------------------------------------------
#LIST COMPHRESION --------------------

# val=[2**i for i in range(1,6)]
# print(val)  o/p [2,4,8,16,32]

#---------------------------------------------------------------------------------------------------------

# s=[i*i for i in range(1,11)]
# print(s)  o/p [1.4.9.16.25.3649.64.81.100]

#--------------------------------------------------------------------------------------------------------

#   DICTIONARY COMPHRESIN 
# squares={x:x*x for x in range(1,6)}
# print(squares)   o/p {1: 1,2,4,3,9,4,16,5,25}

#-----------------------------------------------------------------------------------------------

# doubles={x:2*x for x in range(1,6)}
# print(doubles)

#-----------------------------------------------------------------------------------------------------

#how to read multiple values from the keywords in single line

# a,b= [int(x) for x in input("enter 2 number:").split()]
# print("product is :", a*b)

#-------------------------------------------------------------------------------------------------

# a,b,c= [float(x) for x in input("enter 3 float number :").split(',')]
# print("sum is :", a+b+c)

#-----------------------------------------------------------------------------------------------------


# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item>400:
#         print("this is not in my buget")
#         continue
#     print(item)
# else:
#     print("you have purchased everthing")

#--------------------------------------------------------------------------------------------------
#ask infinte times if password is worng but run only one time 

# username = "admin"
# password = "admin"

# while True:
#     u = input("Enter username: ")
#     p = input("Enter password: ")

#     if u == username and p == password:
#         print("Login Successful")
#         break

#     else:
#         print("Wrong username or password")

#-------------------------------------------------------------------------------------------------------------
#TOWER OF HANOI
# import time

# class Tower:

#     def __init__(self):
#         print("WELCOME TO TOWER OF HANOI GAME")
#         print()

#         print("Given problem    A = [3,2,1]    B = []    C = []")
#         print()

#         print("Expected Output  A = []    B = []    C = [3,2,1]")
#         print()

#         self.A = []
#         self.B = []
#         self.C = []

#     def tower(self, item):
#         self.A.append(item)

#         time.sleep(1)

#         print("A =", self.A)
#         print("Items in Tower A\n")

#     def pass1(self):
#         self.temp = self.A.pop(2)
#         self.C.append(self.temp)

#         time.sleep(1)

#         print("A =", self.A)
#         print("B =", self.B)
#         print("C =", self.C)

#         print("Pass one completed ===================\n")

#     def pass2(self):
#         self.temp = self.A.pop(1)
#         self.B.append(self.temp)

#         time.sleep(1)

#         print("A =", self.A, "   ", "B =", self.B, "   ", "C =", self.C)

#         print("Pass two completed ===================\n")

#     def pass3(self):
#         self.temp = self.C.pop(0)
#         self.B.append(self.temp)

#         time.sleep(1)

#         print("A =", self.A, "   ", "B =", self.B, "   ", "C =", self.C)

#         print("Pass three completed ===================\n")

#     def pass4(self):
#         self.temp = self.A.pop(0)
#         self.C.append(self.temp)

#         time.sleep(1)

#         print("A =", self.A, "   ", "B =", self.B, "   ", "C =", self.C)

#         print("Pass four completed ===================\n")

#     def pass5(self):
#         self.temp = self.B.pop(1)
#         self.A.append(self.temp)

#         time.sleep(1)

#         print("A =", self.A, "   ", "B =", self.B, "   ", "C =", self.C)

#         print("Pass five completed ===================\n")

#     def pass6(self):
#         self.temp = self.B.pop(0)
#         self.C.append(self.temp)

#         time.sleep(1)

#         print("A =", self.A, "   ", "B =", self.B, "   ", "C =", self.C)

#         print("Pass six completed ===================\n")

#     def pass7(self):
#         self.temp = self.A.pop(0)
#         self.C.append(self.temp)

#         time.sleep(1)

#         print("A =", self.A, "   ", "B =", self.B, "   ", "C =", self.C)

#         print("TOWER OF HANOI COMPLETED")


# obj = Tower()

# obj.tower(3)
# obj.tower(2)
# obj.tower(1)

# obj.pass1()
# obj.pass2()
# obj.pass3()
# obj.pass4()
# obj.pass5()
# obj.pass6()
# obj.pass7()

#--------------------------------------------------------------------------------------------------------------------------------- 