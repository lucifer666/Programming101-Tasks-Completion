from palindrome import palindrome

def next_hack(number):
    number += 1
    while(True):
        if palindrome(bin(number)[2:]) and (bin(number)[2:].count('1') % 2 != 0):
            return number
        number += 1

print(next_hack(0))
print(next_hack(10))
print(next_hack(8031))
