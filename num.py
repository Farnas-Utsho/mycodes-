# Importing Library
import numpy as np

# using numpy

# a = np.array([1, 2, 3])
# print(type(a))  # For checking the type
# print(a.shape)  # For checking shape of the array
# print(a.ndim)  # For checking the dimension

# b = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])
# print(type(b))
# print(b.shape)
# print(b.ndim)
# b = np.array([[[1, 2, 3, 4], [6, 7, 8, 9], [10, 11, 12, 13]]])
# print(type(b))
# print(b.shape)
# print(b.ndim)


# print(b.dtype)  # Checking data type
# # Check number of element of an array
# print(b.size)
# # Check memeory bytes consumed by an array
# print(b.nbytes)

print("Array creation")

array1 = np.array([1, 2, 3], dtype="int")
print(array1)

print("Trun all elements of an array with 0")
zero = np.zeros((2, 2), dtype="float")  # here (2,2) represent shape of the array
print(zero)

print("Trun all the element of the array into 1")
one = np.ones((3, 3, 3), dtype="int")
print(one)

print("\nTurn all the elements of The array into the desired number")

full = np.full((3, 3), 5)
print(full)
print("\n Create Identity matrix using function in numpy")

identity = np.identity(3, dtype="int")
print(identity)

print("\n Arrange a customize array")
arange = np.arange(2, 10, 2)  # Here (starting point , end point and step or gap )
print(arange)


print("\nLinespace function works to find out how many number  want in a given range")
linespace = np.linspace(
    1, 13, 10, dtype="int"
)  # start ,end and number of item in this range want  to generate
print(linespace)
print("\n\n Empty function ")
empty = np.empty((3, 10), dtype="int")  # initial an empty function of (n,m,x) dimension
print("\n", empty)

# For intialing value in the array for loop needed

for i in range(7):  # here range must be <=m
    empty[:, i] = i

print("\n After intializing value")
print(empty)
