# list functions

fruits = ["apple", "banana", "cherry"]

# append()
fruits.append("orange")
print(fruits) 

# extend()
fruits.extend(["pear", "grape"])
print(fruits) 

# insert()
fruits.insert(1, "kiwi")  # Insert "kiwi" at index 1
print(fruits) 

# remove()
fruits.remove("banana")
print(fruits)  

# clear()
fruits.clear()
print(fruits) 

# count()
fruits = ["apple", "banana", "cherry", "apple"]
count_of_apple = fruits.count("apple")
print(count_of_apple)  

# index()
fruits = ["apple", "banana", "cherry"]
index_of_banana = fruits.index("banana")
print(index_of_banana) 

# sort()
fruits = ["banana", "cherry", "apple"]
fruits.sort()
print(fruits)  

# reverse()
fruits.reverse()
print(fruits) 

# copy()
fruits_copy = fruits.copy()
print(fruits_copy) 

# list()
numbers = (1, 2, 3)
numbers_list = list(numbers)
print(numbers_list)