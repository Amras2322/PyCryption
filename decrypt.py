import string

# stores all upper case alphabets
all_alphabets = list(string.ascii_uppercase)

keyword = input("Enter Keyword: ")
keyword = keyword.upper()
ciphertext = input("Input Text to Decrypt (remove special characters first!): ")

# converts message to list
ct = []
for i in ciphertext:
    ct.append(i.upper())

# removes default elements
def remove_duplicates(list):
    key = []
    for i in list:
        if i not in key:
            key.append(i)
    return key

keyword = remove_duplicates(keyword)

# Stores the encryption list
encrypting = remove_duplicates(keyword + all_alphabets)

# removes spaces and special characters from the encryption list
encrypting = [i for i in encrypting if i != ' ']
#encrypting = [i for i in encrypting if i.isalnum()]

# maps each element of the message to the encryption list and stores it in plaintext
plaintext = ""
for i in range(len(ct)):
    if ct[i] != ' ':
        plaintext = plaintext + all_alphabets[encrypting.index(ct[i])]
    else:
        plaintext = plaintext + ' '

print("Keyword:", keyword)
print("Ciphered Text:", ciphertext)
print("Message after Deciphering:", plaintext)
