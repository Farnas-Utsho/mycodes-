rent = 1220
gas = 202.55645645
rent = 20000
item1 = "Utsho"
item2 = "Banana"
print(rent + gas)
print("Expense Item : ", item1, item2)

# Numbers in python
print(round(gas, 3))

# String in python
print("Ice Cream")

string = "Lets go harmanos"
print(string)
# string[0] = "K"
# print(string[0]) :python cannot do it like java and and c++;
# print form a index

print(
    string[0:8]
)  # here first number indicates it is included and second number defines excluded .
print(string[5:10])
print(string[5:])  # this will go till end

print("Let's learn python")
print('Hello "world"')

# for address
address = """1 purple street 
new york
usa
"""
print(address)

print("#concationation#")
s1 = "Hello"
s2 = "world"
s3 = 67
print(s1 + "" + s2)
str()
print(s1 + "" + str(s3))


# list on python
print("############# List On python ###############")

item1 = "Bread"
item2 = "Pasta"
item3 = "fruits"
items = ["Bread", "Pasta", "fruits"]

print(items)

print(items[0])

items[0] = "Meat"
items[1] = 150
print(items[0])
print(items[1])


print("# printing from list using range #")
print(items[0:2])
print(items[-1])  # negative index means start from the end
items.append("Butter")  # append at the last
print(items)
items.insert(2, "orange")  # insert in a targeted location (postion,item name)
print(items)
bathroom = ["shampoo", "soap"]
my_cart = items + bathroom  # conacatinate multiple lists
print(my_cart)

# Length of the List
print(len(my_cart))

print("#check /search a item from the list returns boolean result")

print("orange" in items)
print("soda" in items)
