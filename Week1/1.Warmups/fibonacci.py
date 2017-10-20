def fibonacci(number):
   seed_val1 = 1
   seed_val2 = 1
   fibonacci_list = [seed_val1, seed_val2]
   if number == 1:
       fibonacci_list.pop()
       return fibonacci_list
   elif number == 2:
       return fibonacci_list
   number -= 2
   while(number != 0):
       seed_val2 = seed_val2 + seed_val1
       seed_val1 = seed_val2 - seed_val1
       fibonacci_list.append(seed_val2)
       number -= 1
   return fibonacci_list


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(10))
