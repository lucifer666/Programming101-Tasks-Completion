def char_histogram(string):
    histogram = {}
    unique = set(string)
    for char in unique:
        histogram[char] = string.count(char)
    return histogram


print(char_histogram("Python!"))
print(char_histogram("AAAAaaa!!!"))