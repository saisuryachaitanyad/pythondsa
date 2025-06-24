#finding lowest value in an array
my_array = [7, 12, 9, 4, 11]
min = my_array[0]
for i in range(1, len(my_array)):
    if min >= my_array[i]:
        min = my_array[i]
print("The minimum number in the array:", min)

