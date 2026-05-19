
# salary = int(input('enter tyour salary:'))
# rating = int(input('enter your performanceappraisal rating:'))
# increment =0
# if rating >=1 and rating<=3:
#     increment = salary*10/100
# elif rating>=3.1 and rating<=4:
#     increment = salary*30/100
# elif rating>=4.1 and rating<=5:
#     increment = salary*40/100
# else:
#     print('invalid rating')
# print('incremented salary:',increment+salary)

#-------------------------------------------------------------------------------------------------------------------------

# name='aabbbbeeeeeffggg'
# newname=()
# for i in range(len(name)):
#     key = name[i]
# count = 0
# for i in range(len(name)):
# if key ==name[j]:
#     newname[key]=count
# #print(newname)
# for i,j in newname.item(0):
#     print(i,j,sep='',end='') 

#----------------------------------------------------------------------------------------------------------------------------------

#  Q) basicSalary = 20000
# so we have to calcuate
# HRA od basicSalary = 20%
# TA of basicSalary = 30%
# DA of basicSalary = 45%
# calculate Grosssalary =?

# basicSalary = 20000
# HRA = basicSalary * 20 / 100
# TA = basicSalary * 30 / 100
# DA = basicSalary * 45 / 100
# grossSalary = basicSalary + HRA + TA + DA
# print("Basic Salary =", basicSalary)
# print("HRA =", HRA)
# print("TA =", TA)
# print("DA =", DA)
# print("Gross Salary =", grossSalary)
#-----------------------------------------------------------------------------------------------------------------------

#--------------------------------------------Binary Search ------------------------------------------------------------

# def binarysearch(array, target):
#     low = 0
#     high = len(array) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# array = [2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
# target = 72
# result = binarysearch(array, target)
# if result == -1:
#     print("Element not found")
# else:
#     print("Element found at index", result)

#-------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------Bubble sort--------------------------------------------------- 

# def bubblesort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#             print(array)
#         print()


# array =[64,34,25,12,22,11,90]
# bubblesort(array)

#---------------------------------------------------------------------------------------------------------------------

# Find the security key (count of repeated digits)

# mylist =[5,7,8,3,7,8,9,2,3]
# newlist=[]
# for i in range(len(mylist)):
#     count=0
#     key=mylist[i]
#     j=i+1  
#     while j<len(mylist):
#         if key == mylist[j]:
#             newlist.append(key)
#         j=j+1
# print(len(newlist))

#-----------------------------------------------------------------------------------------------------------------------

# class student:
#     def _init_(self):
#         self.name ="geetu"
#         self.age =21

#     def display(self):
#         print("name=" self.name)
#         print("age=", self.age)
# stuObj = student()
# print(stuObj)


# class message():
#     def __init__(self):
#         print("i am constructoe")
#     def shows(self):
#         print("class program")

# obj= message()
# obj.show()
# obj2 = message()

#------------------------parameterized constructor--------------------------------------------------------

# class studentInfo:
#     def __init__(self, name, age, roll):
#         self.name= name
#         self.age=age
#         self.roll= roll
#     def displaystudentInfo(self):
#         print("name=" ,self.name)
#         print("age=",self.age)
    
# studentObj = studentInfo("geetu",21,101)
# studentObj.displaystudentInfo()

#-----------------------------------stack------------------------------------------------------------------------------

# import sys
# class stack:
#     def __init__(self):
#         self.mystack =[]
    
#     def push(self,value):
#         self.mystack.append(value)
#         print("element push:")

#     def display(self):
#         print(self.mystack)
    
#     def isEmpty(self):
#         if self.mystack == []:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             print("stack is empty:")
#         else:
#             print(self.mystack.pop())
    
#     def peek(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.mystack[-1])

#     def deletestack(self):
#         self.mystack =none 

# obj = stack()
# print("stack has created:")
# while True:
#     print("1.push operator:")
#     print("2.display stack:")
#     print("3.pop operation:")
#     print("4.peek")
#     print("5.delete stack")
#     print("7.exit:")
#     choice = int(input("enter your choice:"))
#     if choice == 1:
#         value =int(input("enter value to push in stack:"))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.pop()
#     elif choice ==4:
#         obj.peek()
#     elif choice ==5:
#         obj.deletestack()
#     else:
#         sys.exit(1)

#---------------------------------------------------------------------------------------------------------------

# #  Qcompany wishes to encodes its dala. The data Is in the form of a number They wish to encode the data with respect to a specific digit. They wish to count the number of times the specific digit reoccurs in the given data so that they can encode the data accordingly. Write an algorithm to find the count of the specific digit in the given data.
# Input
# The input consists of two space-separated integers- data and digít, representing the data to be encoded and the digit to be counted in the data.
# Output
# Print an integer representing the courbof the specilic digit.

#oneway-------
# data, digit = map(int, input().split())
# count = 0
# while data > 0:
#     rem = data % 10
#     if rem == digit:
#         count += 1
#     data = data // 10
# print(count)

# mylist =[5,7,2,3,7,8,2,3,3]
# newdict={}
# for i in range(len(mylist)):
#     count=0
#     key=mylist[i]
#     j=1
#     while j<len(mylist):
#         if key == mylist[j]:
#             count+=1
#         j=j+1
#     if count>1:
#         newdict[key]= count

# max= newdict
# print(max)

#----------------------------------------------------------------------------------
# option output 
# 1.add sudent
# 2. show student
# 3. update 
# 4.delete
# 5. exit 
# select my Choice 
# enter student id /rollno/name/city
# update student - 