def caesar_cipher(text, shift, encrypt=True):
    
    result = ""

    for char in text:
        if char.isalpha():  
            if char.isupper():
                start = 65  # ASCII value of 'A'
            else:
                start = 97  # ASCII value of 'a'

            # caesar cipher formula
            if encrypt:
                new_char = chr((ord(char) - start + shift) % 26 + start)
            else:
                new_char = chr((ord(char) - start - shift) % 26 + start)

            result += new_char  
        else:
            result += char  

    return result


mode = input("Type 'e/E' to encrypt or 'd/D' to decrypt: ")

if mode == "e" or mode == "E":
    encrypt = True
elif mode == "d" or mode == "D":
    encrypt = False
else:
    print("Invalid option! Please enter 'e/E' or 'd/D'.")
    exit()  

text = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))

print("Here is your message:", caesar_cipher(text, shift, encrypt))
