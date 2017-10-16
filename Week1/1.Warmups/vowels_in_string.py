vowels = ["a","e","i","o","u","y"]

def count_vowels(word):
    counter = 0
    for letter in word:
        if letter.lower() in vowels:
            counter += 1
    return counter


print(count_vowels("Python"))
print(count_vowels("Theistareykjarbunga"))
print(count_vowels("grrrrgh!"))
print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_vowels("A nice day to code!"))