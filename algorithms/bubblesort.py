#bubble sorting
my_array = [7, 12, 9, 4, 11]
for j in range(len(my_array)-1):
    for i in range(len(my_array)-1):
        if my_array[i] > my_array[i+1]:
            my_array[i], my_array[i+1] = my_array[i+1], my_array[i]
print(my_array)

#improved bubble sorting
my_array = [12, 3, 9, 1, 14]
length = len(my_array) - 1
for i in range(length):
    swapped = False
    for j in range(length-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        break
print("Sorted array:", my_array)