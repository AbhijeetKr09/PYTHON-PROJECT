list_x = [1, 23, 3, 4, 5, 6, 7, 78,54, 3, 23, 3, 34,4 ,45, 3, 4, 34]
length = len(list_x)
number = 0
while number < length:
    print(list_x[number])
    if number < length:
        print(True)
    number += 1
print(number)