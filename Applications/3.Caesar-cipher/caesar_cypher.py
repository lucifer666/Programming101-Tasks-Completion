import string

alphabet = list(string.ascii_lowercase)

def caesar_encrypt(initial_string, number):
	encrypted_string = ""
	for char in initial_string:
		if char.lower() in alphabet:
			new_index = alphabet.index(char.lower()) + number
			if new_index > len(alphabet)-1:
				new_index = number - (len(alphabet) - alphabet.index(char.lower()))
			if (char.isupper()):
				encrypted_string += alphabet[new_index].upper()
			else:
				encrypted_string += alphabet[new_index]
		else:
			encrypted_string += char
	return encrypted_string

   

print(caesar_encrypt("abc", 1))
print(caesar_encrypt("ABC", 1))
print(caesar_encrypt("abc", 2))
print(caesar_encrypt("aaa", 7))
print(caesar_encrypt("xyz", 1))
print(caesar_encrypt("Xy-z", 8))
print(caesar_encrypt("Ab+L", 10))
print(caesar_encrypt("KQ90c", 18))