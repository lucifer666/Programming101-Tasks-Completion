def palindrome(obj):
    obj = str(obj)
    return obj == obj[::-1]

print(palindrome(121))
print(palindrome("kapak"))
print(palindrome("baba"))


