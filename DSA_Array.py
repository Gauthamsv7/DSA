import array as arr

'''
Type Codes for an array : 

int - i
float - f
double - d
unicode - u

'''


#Creating an array

arr_1 = arr.array("i",[1,2,3])
arr_2 = arr.array("d",[1.5,2.7,3.8])
arr_3 = arr.array("u",["a","b","c"])

print(arr_1.typecode)
print(arr_2.typecode)
print(arr_3.typecode)

print(arr_1)
print(arr_2)
print(arr_3)


#Length of an array 

for i in range(0,len(arr_1)):
    print(arr_1[i])
    
    

#Assessing elements from an array using Index values : 

x = list(range(1,10,2))
new_array = arr.array("i",x)

for i in range(0,len(new_array)):
    print(new_array[i],end=" ")
print("\n")


#Adding Elements in an Array

new_array_1 = arr.array("i",[3,4,5,6,7,8,9])
for i in range(0,len(new_array_1)):
    print(new_array_1[i])
print("\n")

#Adding Elements into an Array
new_array_1.insert(0,2)
for i in range(0,len(new_array_1)):
    print(new_array_1[i],end=" ")
print("\n")

#Adding Elements into an Array using Append

new_array_1.append(11)
for i in range(0,len(new_array_1)):
    print(new_array_1[i],end=" ")
print("\n")


#Updating Elements

new_array_1[-1] = 10
for i in range(0,len(new_array_1)):
    print(new_array_1[i],end=" ")
print("\n")


#Deleting element in an array
new_array_1.pop(-1)
for i in range(0,len(new_array_1)):
    print(new_array_1[i],end=" ")
print("\n")

#Remove elements from an array 
new_array_1.remove(6)
for i in range(0,len(new_array_1)):
    print(new_array_1[i],end=" ")
print("\n")


#Slicing

x = list(range(0,50,3))
arr_4 = arr.array("i",x)

#Slicing operations 
arr_4_a = arr_4[10:20]
for i in range(0,len(arr_4_a)):
    print(arr_4_a[i],end=" ")
print("\n")

#reverse the order using slicing :
arr_4_a = arr_4[::-1]
for i in range(0,len(arr_4)):
    print(arr_4_a[i],end=" ")
print("\n")

#Searching an array using Index

y = list(range(0,100,2))
seach_array = arr.array("i",y)

#Print first 10 elements of an Array

for i in range(0,len(seach_array[0:10])):
    print(seach_array[i],end=" ")
print("\n")

#Search the number in the array
index = seach_array.index(46)
search_result = seach_array[index]
print("Index Value : ",index,"& Search Result : ",search_result)

#Sorting an array
arr_5 = arr.array("i",list([5,2,6,7,1,8,3,9]))
arr_5_sorted = arr_5.tolist()

#Ascending Order
arr_5_sorted.sort()
print(arr_5_sorted)

#Descending Order
arr_5_sorted.sort(reverse=True)
print(arr_5_sorted)

#########################################################################   NUMPY   ##############################################################################

import numpy as np

numpy_arr = np.array([1,2,3,4,5])
print(numpy_arr)

print(type(numpy_arr))
print(numpy_arr.shape)

#Creating an array with Zeros
numpy_zeros = np.zeros((2,2))
print(numpy_zeros)

#Creating an array with Ones
numpy_ones = np.ones((2,2))
print(numpy_ones)

#Creating an array with constant Values
numpy_constant = np.full((2,2),5)
print(numpy_constant)

#Creating an Identity Matrix
numpy_identity = np.eye(3)
print(numpy_identity)

#Creating an array with Random Variables
numpy_random = np.random.random((2,2))
print(numpy_random)

########### Zero Dimensional Arrays
Dimensional_zero_array = np.array(1)
print(Dimensional_zero_array)
print(Dimensional_zero_array.ndim,"\n")

########### One Dimensional Arrays
Dimensional_one_array = np.array([1,1])
print(Dimensional_one_array)
print(Dimensional_one_array.ndim,"\n")

########### Two Dimensional Arrays
Dimensional_two_array = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(Dimensional_two_array)
print(Dimensional_two_array.ndim,"\n")

########### Three Dimensional Arrays
Dimensional_three_array = np.array([[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]])
print(Dimensional_three_array)
print(Dimensional_three_array.ndim,"\n")

########### Multi Dimensional Arrays
Dimensional_multi_array = np.array([1,2,3,4,5],ndmin=5)
print(Dimensional_multi_array)
print(Dimensional_multi_array.ndim,"\n")


#CRUD Operations on Numpy Array
#Reading from a numpy array

crud_array = np.array([1,2,3,4,5,6,7,8,9,10])
for i in range(0,len(crud_array)):
    print(i,end=" ")
print("\n")

#Updating an Numpy array with indexing here
crud_array[5] =69
print(crud_array,"\n")

#Deleting elements in an Numpy array
crud_array = np.delete(crud_array,-1)
print(crud_array)
print("\n")

#Seaching Elements in an Numpy array
seaching_in_array = np.array([1,2,3,4,5,6,7,8,9,10])
seaching_in_array_result = np.where(seaching_in_array==7)
print(seaching_in_array_result)
print(seaching_in_array[6]) #Checking if the returning index is true
print("\n")

# Sorting an Numpy array
sorting_an_array = np.array([1,5,2,6,3,7,4,9,8])
sorting_an_array_result_1 = np.sort(sorting_an_array)
print(sorting_an_array_result_1)
print("\n")

#Mathematical Operations
math_op_a = np.array([1,2,3],dtype=np.int64)
math_op_b = np.array([4,5,6],dtype=np.int64)
addition = np.add(math_op_a,math_op_b)
print(addition)
print("\n")

subtraction = np.subtract(math_op_a,math_op_b)
print(subtraction)
print("\n")

multiply = np.multiply(math_op_a,math_op_b)
print(multiply)

divide = np.divide(math_op_a,math_op_b)
print(divide)
print("\n")

square_root = np.sqrt(math_op_a)
print(square_root)
print("\n")

math_transpose = np.transpose(x)
print(math_transpose)
print("\n")
