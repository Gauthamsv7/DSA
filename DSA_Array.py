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

