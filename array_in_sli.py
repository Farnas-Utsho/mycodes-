import numpy as np
#Data scientist 

# Array indexing and slicing
# Here     [ 1 2 3 4 5]
# indexing ( 0 1 2 3 4)
# reverse  (-5 -4 -3 -2 -1 )
arr = np.array([1, 2, 3, 5])
print("\n", arr[2])
print("\n", arr[-1])

print("\n Create a n dimensional array")

arr2 = np.random.randint(1, 20, size=(4, 4))
print(arr2)
print("\n Printing target element")
print(arr2[1][2])

print("\nCreating a 3 dimensional array")
arr3 = np.random.randint(5, 20, size=(2, 3, 3))
print(arr3)
print("\nArray slicing")
print(arr[0:3])
print("\n", arr[:3])  # from index 0 to (n-1)
print("\n", arr[1:])  # from index 1 to last

print("\n\n")

arr4 = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 12], [13, 14, 15, 16]])
print("\n ")
print(arr4)
print("\n Time to slice")
print(arr4[0:2, 0:2])  # Here first pair (0:2) represnt row
# second pair(0:3) represnt column
