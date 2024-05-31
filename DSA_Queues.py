#Implementation of Queue in python using Lists

my_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
my_queue = []
print(my_list)

#Adding Elements in the Queue
for i in range(0,len(my_list)):
    my_queue.append(my_list[i])
    print(my_queue)
    
#Removing Elements from the Queue
for i in range(0,len(my_queue)):
    my_queue.pop(0)
    print(my_queue)
    
#Updating Elements in the Queue
my_queue_1 = [1,2,3,4,5,6,7,8,9]
def update_queue(data,value):
    for i in range(0,len(my_queue_1)):
        if my_queue_1[i] == data:
            my_queue_1[i] = value
            print(my_queue_1)
    return my_queue_1

print(update_queue(3,100))
 
#Implementation of Queue in python using Arrays
import array as arr

my_queue_2 =  arr.array("i",[1,2,3,4,5,6,7,8,9,10])
#Reading the array

for i in my_queue_2:
    print(i,end=" ")
print("\n")

#Inserting elements in the queue
my_queue_2.append(11)
for i in my_queue_2:
    print(i,end=" ")
print("\n")
        
#Removing elements from the queue
for i in range(0,len(my_queue_2)):
    my_queue_2.pop(0)
    for i in my_queue_2:
        print(i,end=" ")
    print("\n")

#Updating elements from the queue using Arrays
my_queue_3 = arr.array("i",[1,2,3,4,5])
def update(data,values):
    index = my_queue_3.index(data)
    my_queue_3[index] = values
    for i in my_queue_3:
        print(i,end=" ")

print(update(5,3))

#Modifying the elements in the queue using Deque
from collections import deque
my_deque = deque([1,2,5,4,5])
def update(data,values):
    for i in range(0,len(my_deque)):
        if my_deque[i] == data:
            my_deque[i] = values
    return (my_deque)

def update_new(data,values):
    index = my_deque.index(data)
    my_deque[index] = values
    return (my_deque)

print(update_new(5,3))

#Sorting a De_Queue
queue_deq = deque([5,3,17,22,34])
queue_arr = arr.array("i",[5,3,17,22,34])
queue_lis = [5,3,17,22,34]

sample = []
def sortdeque():
    for i in range(0,len(queue_deq)):
        res = queue_deq.popleft()
        sample.append(res)
        
    sample.sort()
    for i in sample:
        queue_deq.append(i)
    return queue_deq

sample_arr = []
def sort_arr():
    for i in range(0,len(queue_arr)):
        res = queue_arr.pop(0)
        sample_arr.append(res)
        
    sample_arr.sort()
    for i in sample_arr:
        queue_arr.insert(0,i)
    return queue_arr

def sort_list():
    queue_lis.sort()
    return queue_lis

print(sortdeque())
print(sort_arr())
print(sort_list())

########################    PRIORITY QUEUE ############################

#Taking lowest value as the priority

priority_queue = []
priority_queue.append(10)
priority_queue.append(40)
priority_queue.sort()
priority_queue.append(20)
priority_queue.sort()
print(priority_queue)
for i in range(len(priority_queue)):
    priority_queue.pop(0)
    print(priority_queue)
    
import queue

priority_queue_1 = queue.PriorityQueue()
priority_queue_1.put(10)
priority_queue_1.put(60)
priority_queue_1.put(20)
priority_queue_1.put(40)
priority_queue_1.put(40)

priority_queue_1.get()
priority_queue_1.get()
priority_queue_1.get()

print(priority_queue_1)


########################################    HEAP ###############################

