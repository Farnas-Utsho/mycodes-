# num = int(
#     input("Enter a number : ")
# )  # taking input from the user and converting the string to integer
# if num % 2 == 0:
#     print("Even call")
# else:
#     print("Odd call")


# if 2 == 2 and 4 == 4:
#     print("true")
# else:
#     print("False")


# bangl = ["alo vorta","daal", "vat"]
# indain = ["edli", "dosa", "Hydrabadi biriyani"]
# food = input("Enter a dish name: ")
# if food in bangl:
#     print("Bangladeshi")
# elif food in indain:
#     print("Indian")
# else:
#     print("Does not exist")


print("####### LOOP ########## ")

exp = [2340, 5582, 4567, 5548, 5550, 12358, 789456, 125545569]
total = 0
for i in exp:
    total = total + i

print("Total sum is : ", total)

print("# Range #")
for i in range(1, 11):  # start index and ending index (it will print 1 to 10)
    print(i * i)


exp = [2340, 5582, 4567, 5548, 5550, 12358, 789456, 125545569]
for i in range(len(exp)):
    print("Month : ", (i + 1), "Expense is : ", exp[i])
    total = total + exp[i]


print("Totoal expense is : ", total)

print("# Break in loop")

key_location = "chair"
locations = ["garage", "living room", "chair", "closet"]

for i in locations:
    if i == key_location:
        print("Key is found in: ", i)
        break
    else:
        print("Key is not found in: ", i)


print("# Use of continue #")

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i * i)


print("While loop")

i = 1
while i <= 5:
    print(i)
    i = i + 1
