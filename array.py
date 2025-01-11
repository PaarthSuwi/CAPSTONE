# Importing the array module
import array as arr

# Creating an array of integers
# Syntax: array(typecode, [initializers])
# 'i' is the typecode for integers
a = arr.array('i', [1, 2, 3, 4, 5])

# Accessing elements in an array
# Arrays are zero-indexed, so the first element is at index 0
first_element = a[0]  # Access the first element
second_element = a[1]  # Access the second element

# Modifying elements in an array
a[0] = 10  # Change the first element to 10

# Adding elements to an array
# append() adds an element to the end of the array
a.append(6)  # Adds 6 to the end of the array

# extend() adds multiple elements to the end of the array
a.extend([7, 8, 9])  # Adds 7, 8, and 9 to the end of the array

# insert() adds an element at a specific position
a.insert(2, 20)  # Inserts 20 at index 2

# Removing elements from an array
# pop() removes and returns the last element by default
last_element = a.pop()  # Removes and returns the last element (9)

# pop(index) removes and returns the element at the specified index
element_at_index_2 = a.pop(2)  # Removes and returns the element at index 2 (20)

# remove() removes the first occurrence of a specific value
a.remove(10)  # Removes the first occurrence of 10

# Finding the length of an array
length = len(a)  # Returns the number of elements in the array

# Slicing an array
# Syntax: array[start:stop:step]
slice_of_array = a[1:4]  # Returns elements from index 1 to 3 (exclusive of 4)

# Reversing an array
a.reverse()  # Reverses the order of elements in the array

# Counting occurrences of an element in an array
count_of_5 = a.count(5)  # Returns the number of times 5 appears in the array

# Converting an array to a list
list_from_array = a.tolist()  # Converts the array to a Python list

# Clearing all elements from an array
a = arr.array('i')  # Reinitializes the array to an empty array

# Checking if an array is empty
is_empty = len(a) == 0  # Returns True if the array is empty, False otherwise

# Iterating over an array
for element in a:
    print(element)  # Prints each element in the array

# Copying an array
b = arr.array('i', a)  # Creates a new array 'b' with the same elements as 'a'

# Concatenating arrays
c = arr.array('i', [10, 11, 12])
d = a + c  # Concatenates arrays 'a' and 'c' into a new array 'd'

# Sorting an array
# Note: The array module does not have a built-in sort method, so we convert to a list, sort, and convert back
a_list = a.tolist()
a_list.sort()
a = arr.array('i', a_list)  # Converts the sorted list back to an array

# Finding the index of an element
index_of_5 = a.index(5)  # Returns the index of the first occurrence of 5

# Checking if an element exists in an array
is_5_in_array = 5 in a  # Returns True if 5 is in the array, False otherwise

# Converting an array to a string
array_as_string = a.tobytes()  # Converts the array to a bytes object

# Converting a string (bytes) back to an array
new_array = arr.array('i')
new_array.frombytes(array_as_string)  # Converts the bytes object back to an array

# Printing the array
print(a)  # Prints the entire array