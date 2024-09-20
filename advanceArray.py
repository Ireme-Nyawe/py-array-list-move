import numpy as np

# Create a NumPy array of integers
numpy_array = np.array([1, 2, 3, 4])
print(type(numpy_array))  # Output: <class 'numpy.ndarray'>

# Create a NumPy array of strings
string_array = np.array(["apple", "banana", "cherry"], dtype=str)
print(type(string_array))  # Output: <class 'numpy.ndarray'>

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def display(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data)
#             current_node = current_node.next

# # Example usage:
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
# linked_list.display()  # Output: 1 2 3

# #understanding Self
# class Dog:
#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age    # Instance attribute

#     def bark(self):
#         print(f"{self.name} says Woof!")  # Using self to access the instance's name

# # Create an instance of Dog
# my_dog = Dog("Buddy", 3)

# # Call the bark method
# my_dog.bark()  # Output: Buddy says Woof!
