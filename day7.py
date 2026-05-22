
# print("-------------------------factorial solution---------------------------------")

# def factorial(num):
#     if num <= 1:
#         return 1
#     return num * factorial(num - 1)

# print(factorial(4))

# print("---------------------capitalized using recursion -------------------------------------------")

# def capitalize(arr):

#     result =[]
#     if len(arr) ==0:
#         return result
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalize(arr[1:])
# print(capitalize(['car','taco','banana']))

# print("-----------------------------------------------")

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent-1)

# print(power(2,0)) #1
# print(power(2,2)) #4
# print(power(2,4)) #16

# print("------------productOfArray-------------------------")

# def productofarray(arr):
#     if len(arr) ==0:
#         return 1
#     return arr[0] * productofarray(arr[1:])

# print(productofarray([1,2,3])) #6
# print(productofarray([1,2,3,10]))  #60

# print("---------------------------reverse solu tion---------------------------")

# def reverse(strng):
#     if len(strng) <= 1:
#         return strng
#     return strng[len(strng)-1] +reverse(strng[0:len(strng)-1])

# print(reverse('python')) # 'nohtyp'
# print(reverse('appmilleers'))  # 'srellimppa'

# print("---------------------------recursiverange solution--------------------------------------------")

# def recursiverange(num):
#     if num <=0:
#         return  0
#     return num + recursiverange(num -1)

# print(recursiverange(6)) # 654321

# print("--------------some recursive solution--------------------------------------------------------------")

# def somerecursive(arr, cb):
#     if len(arr) == 0:
#         return False
#     if not(cb(arr[0])):
#         return somerecursive(arr[1:], cb)
#     return True

# def isodd(num):
#     if num%2 ==0:
#         return False
#     else:
#         return True

# print(somerecursive([1,2,3,4] , isodd)) #true
# print(somerecursive([4,6,8,9] , isodd)) #true
# print(somerecursive([4,6,8] , isodd)) #false


# print("--------------Question------------------------")

# n = int(input())
# arr = list(map(int, input().split()))
# # Sort the array
# arr.sort()
# # Product of two largest numbers
# p1 = arr[-1] * arr[-2]
# # Product of two smallest numbers
# # (useful when both are negative)
# p2 = arr[0] * arr[1]

# # Choose the pair with maximum product
# if p1 >= p2:
#     print(arr[-1] + arr[-2])
# else:
#     print(arr[0] + arr[1])
# print()

# print("-----------------TREE IMPLEMENTATION-----------------")

# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.child = []

#     def addchild(self, obj):
#         self.child.append(obj)
#         print("New node added.")

#     def printTree(self, level=0):
#         print(" " * level + self.data)
#         for child in self.child:
#             child.printTree(level + 4)
            
# rootNode = Tree("Drinks")
# Hot = Tree("Hot")
# Cold = Tree("Cold")
# Tea = Tree("Tea")
# Coffee = Tree("Coffee")
# Alco = Tree("Alcoholic")
# NonAl = Tree("Non-Alcoholic")

# rootNode.addchild(Hot)
# rootNode.addchild(Cold)
# Hot.addchild(Tea)
# Hot.addchild(Coffee)
# Cold.addchild(Alco)
# Cold.addchild(NonAl)

# rootNode.printTree()

# print("---------question-----------")

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []

#     # Add child node
#     def add_child(self, child):
#         self.children.append(child)

#     # Print tree
#     def print_tree(self, level=0):
#         print(" " * level * 4 + self.data)

#         for child in self.children:
#             child.print_tree(level + 1)

#     # Find height of tree
#     def height(self):
#         if not self.children:
#             return 0

#         heights = []

#         for child in self.children:
#             heights.append(child.height())

#         return 1 + max(heights)


# # Creating nodes
# N1 = TreeNode("N1")
# N2 = TreeNode("N2")
# N3 = TreeNode("N3")
# N4 = TreeNode("N4")
# N5 = TreeNode("N5")
# N6 = TreeNode("N6")
# N7 = TreeNode("N7")
# N8 = TreeNode("N8")

# # Building tree
# N1.add_child(N2)
# N1.add_child(N3)

# N2.add_child(N4)
# N2.add_child(N5)

# N3.add_child(N6)

# N4.add_child(N7)
# N4.add_child(N8)

# # Print tree
# print("Tree Structure:")
# N1.print_tree()

# # Height of tree
# print("\nHeight of tree =", N1.height())

# print("---------rotate------------1 ")

# def rotateArray(arr, k):

#     n = len(arr)

#     # Handle cases where k > n
#     k = k % n

#     # Rotate array
#     rotated = arr[-k:] + arr[:-k]

#     return rotated


# # Input
# arr = list(map(int, input("Enter array elements: ").split()))
# k = int(input("Enter number of steps: "))

# result = rotateArray(arr, k)

# print("Rotated Array:", result)

