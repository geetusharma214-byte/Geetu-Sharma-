# print("---------Question----------------")
# def remove_zero(arr):
#     result = []
#     started = False

#     for num in arr:
#         # Skip zeros until first non-zero element
#         if not started and num == 0:
#             continue

#         started = True
#         result.append(num)

#     return result


# # Example
# print(remove_zero([0, 0, 0, 1, 2, 3]))      # [1, 2, 3]

#----------------------------------------------------------------------------------------------------------------

# print("-------------Question-------------")

# def firstMissingPositive(nums):
#     n = len(nums)

#     i = 0
#     while i < n:
#         correct_index = nums[i] - 1

#         # Place positive numbers at their correct position
#         if 1 <= nums[i] <= n and nums[i] != nums[correct_index]:
#             nums[i], nums[correct_index] = nums[correct_index], nums[i]
#         else:
#             i += 1

#     for i in range(n):
#         if nums[i] != i + 1:
#             return i + 1

#     return n + 1

# print(firstMissingPositive([3,4,-1,1]))  
# 
# -------------------------------------------------------------------------------------------------------------------
# 
# print("----------------------------------------- binary tree--------------------------------------------")

# Full Binary Tree 
# 1. each node has either 0 or 2 children
# 2. no node has a single child 

# Complete Binary Tree 
# 1 all levels except possibly the last are completely filled
# 2. nodes in the ast level are filled from left to right

# Perfect Binary Tree 
# 1. all internet nodes have exactly two nodes
# 2. all leaf node are at same level 

# print("---------------------Traversing-----------------------------")
# preorder traversing
# root-left-right

# postorder traversing
# left-right-root

# inorder
# left-root-right

# print("---------------------------BINARY SEARCH TREE NODE -----------------------------------")

# class BST:
#     def __init__(self, data):
#         self.data = data
#         self.leftchild = None
#         self.rightchild = None

#     def insert(self, nodevalue):
#         if self.data is None:
#             self.data = nodevalue
#             return

#         # Left subtree
#         if nodevalue <= self.data:
#             if self.leftchild is None:
#                 self.leftchild = BST(nodevalue)
#             else:
#                 self.leftchild.insert(nodevalue)

#         # Right subtree
#         else:
#             if self.rightchild is None:
#                 self.rightchild = BST(nodevalue)
#             else:
#                 self.rightchild.insert(nodevalue)
# def preorder(root):
#     if root is None:
#         return
#     print(root.data, end=" ")
#     preorder(root.leftchild)
#     preorder(root.rightchild)

# def postorder(root):
#     if root is None:
#         return
#     postorder(root.leftchild)
#     postorder(root.rightchild)
#     print(root.data , end=" ")
# def inorder(root):
#     if root is None:
#         return 
#     inorder(root.leftchild)
#     print(root.data , end=" ")
#     inorder(root.rightchild)  
    
# # Function to search a node in BST

# def search(root, value):
#     # If tree is empty
#     if root is None:
#         return False
#     # Value found
#     if root.data == value:
#         return True
#     # Search in left subtree
#     elif value < root.data:
#         return search(root.leftchild, value)
#     # Search in right subtree
#     else:
#         return search(root.rightchild, value)
    
# # Function to print tree
# def printTree(root, space=0, level_space=5):
#     if root is None: 
#         return
#     # Print right child first
#     printTree(root.rightchild, space + level_space)
#     # Print current node
#     print()
#     print(" " * space + str(root.data))
#     # Print left child
#     printTree(root.leftchild, space + level_space)


# # Create BST
# newBST = BST(None)

# # Insert nodes
# newBST.insert(70)
# newBST.insert(50)
# newBST.insert(90)
# newBST.insert(30)
# newBST.insert(60)
# newBST.insert(80)
# newBST.insert(100)
# newBST.insert(20)
# newBST.insert(40)

# # Print tree
# printTree(newBST)
# print("Preorder Traversal : ")
# preorder(newBST)
# print()

# print("Inorder Traversal : ")
# inorder(newBST)
# print()

# print("Postorder Traversal : ")
# postorder(newBST)

# print()
# if search(newBST, 60):
#     print("Node Found")
# else:
#     print("Node Not Found")
# if search(newBST, 200):
#     print("Node Found")
# else:
#     print("Node Not Found")  

# print("--------Exception Handling---------")
# try:
#     a = int(input("Enter a number : "))
#     b = int(input("Enter another number : "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Can't divide by zero!") 
# except ValueError:
#     print("Enter only an integer value .")
    
# #or
# try:
#     a = int(input("Enter a number : "))
#     b = int(input("Enter another number : "))
#     print(a/b)
# except(ZeroDivisionError , ValueError) as msg:
#     print(msg)

# print("--------Exception Handling---------")
# import logging

# logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)

# try:
#     a = int(input("enter first integer no"))
#     b = int(input("enter second integer no"))
    
#     print(a / b)

# except (ZeroDivisionError, ValueError) as message:
#     print(message)
#     logging.exception(message)

# print("Logging Level is set up. Check 'newfile.txt' for log details.")

#-----------------------------------------------------------------------------------------------------------------
# import csv

# f = open("employee.csv", 'a')

# a = csv.writer(f)

# a.writerow(["EmpID", "Emp Name", "Emp Age"])

# empid = int(input("Enter your Empid : "))
# empName = input("Enter employee name : ")
# age = int(input("Enter employee age : "))

# a.writerow([empid, empName, age])

# print("file has created")

# f.close()
#---------------------------------------------------------------------------------------------------------------

