import time

def fib(x):
    num1 = 0
    num2 = 1
    count = 0

    while (count < x - 1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        count += 1
    
    print(num3)
    print(f'fib({x}) took {time.process_time()} seconds')
    
fib(34)