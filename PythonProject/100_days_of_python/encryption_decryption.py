# print(ord('a'))97
# print(ord('z'))122
# print(ord('A'))65
# print(ord('Z'))90

def encrypt_decrypt(message, shift, encrypt = True):
    char = ""
    shift = shift if encrypt else -shift
    for i in message:
        if i.isupper():
            shifted_char = chr((ord(i) + shift)%90+64) if (ord(i) + shift) > 90 else chr(ord(i) + shift)
            char += shifted_char
        elif i.islower():
            shifted_char = chr((ord(i) + shift) % 122 + 96) if (ord(i) + shift) > 122 else chr(ord(i) + shift)
            char += shifted_char

    if encrypt:
        print("Your encrypted message is: ", char)
    else:
        print("Your decrypted message is: ", char)
encrypt_decrypt("vxplwkd", 3, False)


