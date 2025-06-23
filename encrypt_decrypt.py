import random
import string
chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()

random.shuffle(key)
text=input("Enter a text")
cipher_text=""
#ENCRYPT
for letter in text:
    indexvalue=chars.index(letter)
    cipher_text+=key[indexvalue]
print(cipher_text)
originaltext=""
#DECRYPT
for letter1 in cipher_text:
    index=key.index(letter1)
    originaltext+=chars[index]
print(originaltext)
