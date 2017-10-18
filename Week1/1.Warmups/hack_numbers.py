def next_hack(n):
    is_hack_number = False
    n += 1
    while(is_hack_number == False):
        if (bin(n)[2:] == bin(n)[2:][::-1]) and (bin(n)[2:].count('1') % 2 != 0):
            is_hack_number = True
            return n
        n += 1


print(next_hack(0))
print(next_hack(10))
print(next_hack(8031))
