# Json=java Scripted Object Notation
# {
# "name":"tom",
# "Address": "Dahaka"
# "Phone": "1254678"
# }
book = {}  # dictonary
book["Tom"] = {"name": "tom", "Address": "Dahaka", "Phone": 1254678}
book["Kim"] = {"name": "kim", "Address": "Russsia", "Phone": 125454678}
import json

s = json.dumps(book)  # dumping in json formate
with open("D://Python Basic//json.txt", "w") as f:
    f.write(s)


print("Redaing from json")
f = open("D:\Python Basic\json.txt", "r")
s = f.read()
print(s)
