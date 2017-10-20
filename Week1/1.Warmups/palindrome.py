def palindrome(obj):
    return str(obj) == str(obj)[::-1]

print(palindrome(121))
print(palindrome("kapak"))
print(palindrome("baba"))


