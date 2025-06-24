#fibonacci series implementation using loop
prev2 = 0
prev1 = 1
print(prev2)
print(prev1)
for fibo in range(10):
    fibo_num = prev2 + prev1
    print(fibo_num)
    prev2 = prev1
    prev1 = fibo_num
print('----')

#fibonacci series implementation using recursion
prev2 = 0
prev1 = 1
count = 0
print(prev2)
print(prev1)
def print_fibo(prev2, prev1):
    global count
    if count < 10:
        fibo_num = prev2 + prev1
        print(fibo_num)
        prev2 = prev1
        prev1 = fibo_num
        count+=1
        return print_fibo(prev2, prev1)


print_fibo(prev2, prev1)
print('----')

#fibonacci implementation with recursion using memorization
def fibonacci_memory(n):
    if n <= 1:
        return n
    else:
        return fibonacci_memory(n-1) + fibonacci_memory(n-2)

for i in range(12):
    print(fibonacci_memory(i))