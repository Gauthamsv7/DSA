s = []

s.append("https://github.com/Gauthamsv7/DSA/tree/master")
s.append("https://www.geeksforgeeks.org/")
s.append("https://authn.edx.org/login?next=2Fdashboard")
s.append("https://authn.edx.org/2Fdashboard")
print(s)
s.pop()
print(s)


###############################         Deque ################################

from collections import deque
stack = deque()
stack.append("Link1")
stack.append("Link2")
stack.append("Link3")
stack.append("Link4")
print(stack)
stack.pop()
print(stack)

# class Stack:
#     def __init__(self):
#         self.containers = deque()
#     def push(self,val):
#         self.containers.append(val)
#     def pop(self):
#         return self.containers.pop()
#     def peek(self):
#         return self.containers[-1]
#     def is_empty(self):
#         return len(self.containers)== 0
#     def size(self):
#         return len(self.containers)
   
#     def reverse_string(self,str):
#         for i in str:
#             s.push(i)
#         rstr = ""
#         while s.size() != 0:
#             rstr += s.pop()
#         return rstr
    
#     def is_match(ch1, ch2):
#         match_dict = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }
#         return match_dict[ch1] == ch2
    
#     def is_balanced(s):
#         stack = Stack()
#         for ch in s:
#             if ch=='(' or ch=='{' or ch == '[':
#                 stack.push(ch)
#             if ch==')' or ch=='}' or ch == ']':
#                 if stack.size()==0:
#                     return False
#                 if not is_match(ch,stack.pop()):
#                     return False

#         return stack.size()==0
    
# s = Stack()
# print(s.push(5))
# print(s.peek())
# print(s.peek())
# print(s.pop())
# print(s.is_empty())
# print(s.reverse_string("Gautham"))
# print(s.is_balanced("({a+b})"))


my_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday"]
my_stack = []
print(my_list)

#Stack Appending
for i in range(0, len(my_list)):
    my_stack.append(my_list[i])
    print(my_stack)

#Stack Popping
for i in range(0, len(my_list)):
    my_stack.pop()
    print(my_stack)

#Stack Updating
my_stack = [1,2,3,4,5]
def update(data,value):
    for i in range(0, len(my_stack)):
        if my_stack[i] == data:
            my_stack[i] = value
    return my_stack
print(update(5,10))


#Implementing stacks in python
import array as arr

my_stack = arr.array("i",[1,2,3,4,5,6,7,8,9,10])

#reading the array/stack
for i in my_stack:
    print(i,end=" ")
print("\n")

#Inserting values into the stack

my_stack.append(11)
for i in my_stack:
    print(i,end=" ")
print("\n")

#Deleting values from the stack

for i in range(0,len(my_stack)):
    my_stack.pop()
    for i in my_stack:
        print(i,end=" ")
    print("\n")

#Updating values from the stack

stack = arr.array("i",[1,2,3,4,5])
def update(data,value):
    index = stack.index(data)
    stack[index] = value
    for i in stack:
        print(i,end=" ")
print(update(5,3))


#Implementing stacks in python using Deque

from collections import deque
stack = deque()
my_list = ["A","B","C","D","E","F","G","H","I"]

#Inserting Values into Stack

for i in my_list:
    stack.append(i)
    print(stack)
print("\n")

#Reading Values from Stack

for i in stack:
    print(i,end=" ")
print("\n")

#Deleting Values from Stack

for i in range(0,len(stack)):
    stack.pop()
    print(stack)
    # for i in stack:
    #     print(i,end=" ")
    # print("\n")
    
    
#Updating Values from Stack
stack_update = deque([1,2,3,4,5])
def update(data,value):
    index = stack_update.index(data)
    stack_update[index] = value
    return stack_update
print(update(4,3))

#Sort Values from Stack using Deque
stack_deq = deque([11,2,3,4,5])
stack_arr = arr.array("i",[1,22,3,4,5])
stack_list = [1,2,33,4,5]

#Sorting Values from Stack using Deque
sample = []
def sort_deq():
    for i in range(0,len(stack_deq)):
       x = stack_deq.pop()
       sample.append(x)
    sample.sort()
    for i in sample:
        stack_deq.append(i)
    return stack_deq
   
print(sort_deq())


#Sorting Values from Stack using Array
samples = []
def sort_arr():
    for i in range(0,len(stack_arr)):
        x = stack_arr.pop()
        samples.append(x)
    samples.sort()
    for i in samples:
        stack_arr.append(i)
    return stack_arr

def sort_list():
    stack_list.sort()
    return stack_list

print(sort_arr())

#Sorting Values from Stack using Lists
def sort_list():
    stack_list.sort()
    return stack_list

print(sort_list())

