def sum(item):
    total = 0
    print("Lets go")

    for i in item:
        total = total + i

    return total


tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

toms_total = sum(tom_exp_list)
joes_total = sum(joe_exp_list)

print("Toms total : ", toms_total)
print("Joe's total: ", joes_total)


def addition(a, b):
    print("A is : ", a)
    print("B is : ", b)
    total = a + b
    return total


n = addition(5, 6)
print("Sumation is : ", n)



#
