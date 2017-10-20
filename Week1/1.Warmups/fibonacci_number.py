from fibonacci import fibonacci

def fib_number(number):
    fibonacci_list = fibonacci(number)
    return ("".join([str(num) for num in fibonacci_list]))

print(fib_number(3))
print(fib_number(10))
