import string

# stores all upper case alphabets
all_alphabets = list(string.ascii_uppercase)

keyword = input("Enter Keyword: ")
keyword = keyword.upper()
plaintext = input("Input Text to Encrypt: ")

# converts message to list
pt = []
for i in plaintext:
  pt.append(i.upper())

# removes duplicate elements
def duplicates(list):
  key = []
  for i in list:
      if i not in key:
          key.append(i)
  return key

keyword = duplicates(keyword)

# Stores the encryption list
encrypting = duplicates(keyword + all_alphabets)

# removes spaces from the encryption list
encrypting = [i for i in encrypting if i != ' ']

# maps each element of the message to the encryption list and stores it in ciphertext
ciphertext = ""
for char in pt:
  if char != ' ':
      ciphertext += encrypting[all_alphabets.index(char)]
  else:
      ciphertext += ' '

print("Keyword:", keyword)
print("Message before Ciphering:", plaintext)
print("Ciphered Text:", ciphertext)