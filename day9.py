# print("------IMPLEMENTATION OF LL USING STACK-------")
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def __iter__(self):
#         curnode = self.head
#         while curnode:
#             yield curnode
#             curnode = curnode.next

# class Stack:
#     def __init__(self):
#         self.LinkedList = LinkedList()
#     def isEmpty(self):
#         return self.LinkedList.head is None
#     def __str__(self):
#         values = []
#         current = self.LinkedList.head
#         while current:
#             values.append(str(current.value))
#             current = current.next
#         return '\n'.join(values)
#     def pop(self):
#         if self.isEmpty():
#             return "There is no element in the stack."
#         nodeValue = self.LinkedList.head.value
#         self.LinkedList.head = self.LinkedList.head.next
#         return nodeValue
#     def peek(self):
#         if self.isEmpty():
#             return "There is no element in the stack."
#         return self.LinkedList.head.value
#     def push(self, value):
#         node = Node(value)
#         node.next = self.LinkedList.head
#         self.LinkedList.head = node
#     def delete(self):
#         self.LinkedList.head = None

# # Driver Code
# customStack = Stack()
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# print(customStack)
# print("Top Element:", customStack.peek())
# print("Popped Element:", customStack.pop())
# print("\nAfter Pop:")
# print(customStack)
# print()

# print("--------------ENQUEUE-------------------------")
# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None
        
#     def __str__(self):
#         return str(self.value)

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode
#             curNode = curNode.next

# class Queue:
#     def __init__(self):
#         self.LinkedList = LinkedList()
#     def __str__(self):
#         values = [str(x) for x in self.LinkedList]
#         return ' '.join(values)
#     def enqueue(self, value):
#         newnode = Node(value)
#         if self.LinkedList.head is None:
#             self.LinkedList.head = newnode
#             self.LinkedList.tail = newnode
#         else:
#             self.LinkedList.tail.next = newnode
#             self.LinkedList.tail = newnode
#     def isEmpty(self):
#         return self.LinkedList.head is None
#     def dequeue(self):
#         if self.isEmpty():
#             return "There is not any node in the queue."
#         else:
#             tempnode = self.LinkedList.head
#             if self.LinkedList.head == self.LinkedList.tail:
#                 self.LinkedList.head = None
#                 self.LinkedList.tail = None
#             else:
#                 self.LinkedList.head = self.LinkedList.head.next
#             return tempnode
#     def peek(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         return self.LinkedList.head
#     def delete(self):
#         self.LinkedList.head = None
#         self.LinkedList.tail = None

# # Testing
# custQueue = Queue()
# custQueue.enqueue(1)
# custQueue.enqueue(2)
# custQueue.enqueue(3)
# print(custQueue)
# print("Dequeued:", custQueue.dequeue())
# print(custQueue)
# print("Peek:", custQueue.peek())
# print("Dequeued:", custQueue.dequeue())
# print(custQueue)
# print("Peek:", custQueue.peek())
# print("Dequeued:", custQueue.dequeue())
# print(custQueue)
# print("Peek:", custQueue.peek())
# print() 

# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list.keys():
#             self.adjacency_list[vertex] = []
#             return True
#         return False
    
#     def add_edge(self, vertex1, vertex2):
#         if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
#             self.adjacency_list[vertex1].append(vertex2)
#             return True
#         return False
    
#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex, ":", self.adjacency_list[vertex])

#     def remove_vertex(self, vertex):
#         if vertex in self.adjacency_list.keys():
#             for other_vertex in self.adjacency_list.keys():
#                 if vertex in self.adjacency_list[other_vertex]:
#                     self.adjacency_list[other_vertex].remove(vertex)
#             del self.adjacency_list[vertex]
#             return True
#         return False        

# mygraph = Graph()
# mygraph.add_vertex("A")
# mygraph.add_vertex("B")            
# mygraph.add_vertex("C")
# mygraph.add_vertex("D")
# mygraph.add_vertex("E")

# mygraph.add_edge("A", "B")
# mygraph.add_edge("A", "C")
# mygraph.add_edge("A", "D")

# mygraph.add_edge("B", "A")
# mygraph.add_edge("B", "E")

# mygraph.add_edge("C", "A")
# mygraph.add_edge("C", "D")

# mygraph.add_edge("D", "A")
# mygraph.add_edge("D", "C")
# mygraph.add_edge("D", "E")

# mygraph.add_edge("E", "B")
# mygraph.add_edge("E", "D")
# mygraph.print_graph()

# print("---------Static Method----------")
# class Student :
#     @staticmethod
#     def get_personal_details(firstname , lastname):
#         print("Your personal details : " , firstname,lastname)
#     @staticmethod
#     def contact_details(mobile_no , roll_no):
#         print("Your contact details : " , mobile_no , roll_no)
        
# Student.get_personal_details("Prashant","Jha")
# Student.contact_details(9521563654 , 1011)
# print()

# print("--------SINGLE INHERITANCE---------")
# class College:
#     def college_name(self):
#         print("RBU")
        
# class Student(College):
#     def Student_info(self):
#         print("Name : Harsha Dubey")
#         print("Branch : MCA")
        
# obj = Student()
# obj.college_name()
# obj.Student_info()
# print()

# print("---------MULTI-LEVEL INHERITANCE---------")
# class College:
#     def college_name(self):
#         print("RBU")
        
# class Student(College):
#     def Student_info(self):
#         print("Name : Harsha Dubey")
#         print("Branch : MCA")
        
# class Exam(Student):
#     def subject(self):
#         print("Subject1 : OR")
#         print("Subject2 : Math")
        
# obj1 = Exam()
# obj1.college_name()
# obj1.Student_info()
# obj1.subject()
# print()


# print("----------MULTIPLE INHERITANCE-----------")
# class Submarks:
#     math = int(input("Enter marks of maths : "))
#     DE = int(input("Enter marks of DE : "))

# class PractMarks :
#     cpract = int(input("Enter practical marks of DE : "))

# class result(Submarks,PractMarks):
#     def total(self):
#         if self.math >= 40 and self.DE >= 40 and self.cpract >= 20 :
#             print("Pass")
#         else:
#             print("Fail")
 
# obj2 = result()
# obj2.total()
# print()

