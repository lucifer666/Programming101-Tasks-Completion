def count_words(arr):
    return {word: arr.count(word) for word in set(arr)}

print(count_words(["apple", "banana", "apple", "pie"]))
print(count_words(["python", "python", "python", "ruby"]))
