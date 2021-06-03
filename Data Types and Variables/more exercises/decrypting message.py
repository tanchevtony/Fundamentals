key = int(input())
number_of_lines = int(input())
decrypted = ""
for symbol in range(number_of_lines):
    letter = input()
    encrypt = ord(letter) + key
    decrypted += chr(encrypt)
print(decrypted)