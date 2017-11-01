def is_an_bn(word):
    number_of_a = word.count('a')
    number_of_b = word.count('b')
    if number_of_a != number_of_b:
        return False
    return ("a" * number_of_a + "b" * number_of_b) == word


print(is_an_bn(""))
print(is_an_bn("rado"))
print(is_an_bn("aaabb"))
print(is_an_bn("aaabbb"))
print(is_an_bn("aabbaabb"))
print(is_an_bn("bbbaaa"))
print(is_an_bn("aaaaabbbbb"))