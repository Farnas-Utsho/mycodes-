file = open("D:\\Python Basic\\file.txt", "a")
# file (name,path) and (open mode)
# Here for adding more lines on a single file I need to use append instead of write
file.write("\nLets go People")  # writing on the file
file.close()

f = open("D:\\Python Basic\\read.txt", "r")
# s = f.read()
# print(s)
# we can also read from a file line by line
# Usin g for loop
# for line in f:
#     words = line.split(
#         " "
#     )  # spliting sentences based on space by using splite function
#     # Then stored them in a dic
#     # print(str(words)) here printing the dic
#     print(
#         len(words)
#     )  # countin the number of words for each line which were held on the dic
f_out = open("D:\\Python Basic\\wordcount.txt", "w")
for line in f:
    words = line.split()
    f_out.write(" Words: " + str(len(words)) + ": " + line)


f.close()
f_out.close()
