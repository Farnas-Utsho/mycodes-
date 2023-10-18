# dictonary allows us to store key value
# also known as maps,hastables

d = {
    "Ustho": 5685466,
    "Alpha": 98543,
    "Greeb": 65465460,
    "Rob": 584646,
    "tom": 45445456,
}
print(d["Ustho"])

print("Adding new Item in dic::")
d["Sam"] = 65648464646
print(d)

print("Deleting item")
del d["Greeb"]
print(d)
print(" Printing values ")
for key in d:
    print("Keys: ", key, "Values: ", d[key])

print(" Printing values(easy and funny) ")
for k, v in d.items():
    print("Key: ", k, "value: ", v)

print("Check exsiting ")
if "Ustho" in d:
    print("True")
else:
    print("False")


print("Clear the dic")  # using .clear fuction

d.clear()
print(d)

print(" Tuples ")#every value has different meaning (address,coordinate)
point=(0,9)#here 0 is X cordinate and 9 is y coordinate

