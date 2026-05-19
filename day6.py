
# print("--------Practise questions---------")
# #Reverse each word in a string 
# s = "Hello World"
# words = s.split()
# for i in range(len(words)):
#     words[i] = words[i][::-1]
# result = " ".join(words)
# print(result)
# print()

# #check for valid parenthesis 
# def valid_parenthesis(s):
#     stack = []
#     for ch in s:
#         if ch in "({[":
#             stack.append(ch)
#         elif ch == ")":
#             if not stack or stack[-1] != "(":
#                 return False
#             stack.pop()        
#         elif ch == "}":
#             if not stack or stack[-1] != "{":
#                 return False
#             stack.pop()        
#         elif ch == "]":
#             if not stack or stack[-1] != "[":
#                 return False
#             stack.pop()
#     return len(stack) == 0
# # Example
# s = "{[()]}"
# print(valid_parenthesis(s))

#--------------------------------------------------------------------------------------------------------------
#insertion sort-----------------------------

# def insertion_sort(arr):

#     for i in range(1, len(arr)):

#         key = arr[i]
#         j = i - 1

#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j = j - 1

#         arr[j + 1] = key

#     return arr


# arr = list(map(int, input("Enter numbers: ").split()))

# sorted_arr = insertion_sort(arr)

# print("Sorted array:", sorted_arr)
#----------------------------------------------------------------------------------------------------------------
#selection sort-----------------------------------------------------------------

# print("----------SELECTION SORT------------")

# def selection_sort(arr):

#     n = len(arr)

#     for i in range(n):

#         # Assume current index has minimum value
#         min_index = i

#         # Find smallest element in remaining array
#         for j in range(i + 1, n):

#             if arr[j] < arr[min_index]:
#                 min_index = j

#         # Swap elements
#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr


# # Input
# arr = list(map(int, input("Enter numbers: ").split()))

# # Sorting
# sorted_arr = selection_sort(arr)

# # Output
# print("Sorted array:", sorted_arr)

#---------------------------------------------------------------------------------------------------------------
#findall duplicate in a list 

# class FindDuplicate:
#     def __init__(self, arr):
#         self.arr = arr

#     def duplicates(self):
#         dup = []

#         for i in range(len(self.arr)):
#             for j in range(i + 1, len(self.arr)):
#                 if self.arr[i] == self.arr[j]:
#                     if self.arr[i] not in dup:
#                         dup.append(self.arr[i])

#         return dup


# # Driver Code
# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]

# obj = FindDuplicate(numbers)

# print("Original List:", numbers)
# print("Duplicate Elements:", obj.duplicates())

#-----------------------------------------------------------------------------------------------------------------
#sort dictionary  key or value 
#sample input  ["C",3,"B",2, "A", 1]

# class DSA:
#     def __init__(self):
#         self.mydict = {"C": 3, "B": 2, "A": 1}

#     def sort_key(self):
#         print(sorted(self.mydict.items()))

#     def sort_value(self):
#         print(sorted(self.mydict.items(), key=lambda x: x[1]))


# obj = DSA()

# print("Sort By Key:")
# obj.sort_key()

# print("Sort By Value:")
# obj.sort_value()

#------------------------------------------------------------------------------------------------------------------------
# print("----------Instance Variable-----------")
# #creates a separate memory for each object 
# class New: 
#     def __init__(self):
#         self.a = 10

# obj = New()
# obj1 = New()
# obj2 = New()
# obj.a = 20
# print(obj.a)
# print(obj1.a)
# print(obj2.a)
# print()

# print("-----static variable------")
# class New:
#     a = 10
#     def __init__(self):
#         self.name = "oraora"
# obj3 = New()
# print(obj3.a)
# obj4 = New()
# print(obj4.a)
# New.a = 50
# print(obj3.a)
# print(obj4.a)
# print(New.a)
#--------------------------------------------------------------------------------------------------------------------------
# print("----------------------------------------------------------------------------------------------------")

# class College:
#     collegename = "modern college"
#     def __init__(self):
#         self.studentname = "prashant"
# principal = College()
# teacher = College()
# accountant = College()
# print("principal", principal.collegename, ".......", principal.studentname)
# print("teacher", teacher.collegename, ".......", teacher.studentname)
# print("accountant", accountant.collegename, ".......", accountant.studentname)
# College.collegename = "HBO"
# principal.studentname = "prashant jha"
# print("principal", principal.collegename, "|", principal.studentname)
# print("teacher", teacher.collegename, "|", teacher.studentname)
# print("accountant", accountant.collegename, "|", accountant.studentname)
# print()

#-----------------------------------------------------------------------------------------------------------------
#print("-------------------------------------------------------------------------------------------------------------------" )

# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class linkedlist:
#     def __init__(self):
#         self.head = None
# linkedlist = linkedlist()
# linkedlist.head = node(5)
# second = node(10)
# third = node(15) 
# fourth = node(20)

# linkedlist.head.next = second
# second.next = third
# third.next = fourth

# while linkedlist.head.next != None:
#     print(linkedlist.head.data, "|",linkedlist.head.next," -> ",end=" ")
#     linkedlist.head = linkedlist.head.next 

#------------------------------------------------------------------------------------------------------
#----------Linked list -----------------------------------
# class node:
#     def __init__(self, data):
#         self.data = data   #instance variable
#         self.next = None

# class linkedlist:
#      def __init__(self):
#         self.head = None
#         self.tail = None

#      def addnode(self, value):
#         self.node = node(value) 
 

# if __name__== '__main__':
#     object = linkedlist()

#     while True:
#         print("1. add node linkedlist :")
#         print("2. add node in beginning :")
#         print("3. add node in between :")
#         print("4. add node in end :")
#         print("5. display linkedlist :")
#         print("6. exit :")
#         ch = int(input("enter your choice :"))
#         if ch == 1:
#             value = int(input("enter value for node :"))
#             object.addnode(value)
#             print("node added sucefully in single lnkedlist")


# print("-----LL-----")


# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:

#     def __init__(self):
#         self.head = None
#         self.tail = None

#     # Add node at end
#     def add_end(self, value):

#         new_node = Node(value)

#         if self.head is None:

#             self.head = new_node
#             self.tail = new_node

#         else:

#             self.tail.next = new_node
#             self.tail = new_node

#     # Add node at beginning
#     def add_begin(self, value):

#         new_node = Node(value)

#         if self.head is None:

#             self.head = new_node
#             self.tail = new_node

#         else:

#             new_node.next = self.head
#             self.head = new_node

#     # Add node in between
#     def add_between(self, target, value):

#         while self.head:

#             if self.head.data == target:

#                 new_node = Node(value)

#                 new_node.next = self.head.next
#                 self.head.next = new_node

#                 if self.head == self.tail:
#                     self.tail = new_node

#                 print("Node inserted successfully")
#                 return

#             self.head = self.head.next

#         print("Target node not found")

#     # Delete first node
#     def delete_begin(self):

#         if self.head is None:

#             print("Linked List is empty")
#             return

#         self.head = self.head.next

#         if self.head is None:
#             self.tail = None

#         print("First node deleted")

#     # Delete last node
#     def delete_end(self):

#         if self.head is None:

#             print("Linked List is empty")
#             return

#         if self.head.next is None:

#             self.head = None
#             self.tail = None

#             print("Last node deleted")
#             return

#         while self.head.next != self.tail:
#             self.head = self.head.next

#         self.head.next = None
#         self.tail = self.head

#         print("Last node deleted")

#     # Search node
#     def search(self, value):

#         pos = 1

#         while self.head:

#             if self.head.data == value:

#                 print("Node found at position", pos)
#                 return

#             self.head = self.head.next
#             pos += 1

#         print("Node not found")

#     # Count nodes
#     def count(self):

#         cnt = 0

#         while self.head:

#             cnt += 1
#             self.head = self.head.next

#         print("Total nodes:", cnt)

#     # Display linked list
#     def display(self):

#         while self.head:

#             print(self.head.data, end=" -> ")
#             self.head = self.head.next

#         print("None")


# if __name__ == '__main__':

#     obj = LinkedList()

#     while True:

#         print("\n====== LINKED LIST MENU ======")
#         print("1. Add node at end")
#         print("2. Add node at beginning")
#         print("3. Add node in between")
#         print("4. Delete first node")
#         print("5. Delete last node")
#         print("6. Search node")
#         print("7. Count nodes")
#         print("8. Display linked list")
#         print("9. Exit")

#         ch = int(input("Enter your choice: "))

#         if ch == 1:

#             value = int(input("Enter value: "))
#             obj.add_end(value)

#         elif ch == 2:

#             value = int(input("Enter value: "))
#             obj.add_begin(value)

#         elif ch == 3:

#             target = int(input("Insert after value: "))
#             value = int(input("Enter new value: "))

#             obj.add_between(target, value)

#         elif ch == 4:

#             obj.delete_begin()

#         elif ch == 5:

#             obj.delete_end()

#         elif ch == 6:

#             value = int(input("Enter value to search: "))
#             obj.search(value)

#         elif ch == 7:

#             obj.count()

#         elif ch == 8:

#             obj.display()

#         elif ch == 9:

#             print("Program exited")
#             break

#         else:

#             print("Invalid choice")

