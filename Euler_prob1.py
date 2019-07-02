temp = []
def list_of_multiples(temp):
    for i in range (1000):
        if i % 3 == 0 or i % 5 == 0:
            temp.append(i)
    return temp

list_of_multiples(temp)
total = sum(temp)
print(total)
