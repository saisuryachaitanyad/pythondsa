#selection sort implementation
my_array = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(my_array)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_array[min_index] > my_array[j]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)
    
print("Sorted Array:", my_array)

#better implementation of selection sort
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if my_array[min_index] > my_array[j]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
print("Sorted array:", my_array)