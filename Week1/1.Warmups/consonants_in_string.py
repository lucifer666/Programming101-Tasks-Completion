consonants = list("bcdfghjklmnpqrstvwxz")

def count_consonants(word):
    counter = 0
    for char in word:
    	if char.lower() in consonants:
    		counter += 1
    return counter

print(count_consonants("Python"))
print(count_consonants("Theistareykjarbunga"))
print(count_consonants("grrrrgh!"))
print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_consonants("A nice day to code!"))