plaintext = ""
ciphertext = ""
EN = 0
EN = int(input("Please specify operation. Input 1 for encryption, input 0 for decryption: "))
key = input("Please input key: ")

if EN:
    #encryption
    try:
        f = open("PlainText.txt", "r")
    except FileNotFoundError:
        print("Error: PlainText.txt not found!")
    else:
        plaintext = f.read()
        f.close()
        print("PlainText successfully retrieved")
else:
    #decryption
    try:
        f = open("CipherText.txt", "r")
    except FileNotFoundError:
        print("Error: CipherText.txt not found!")
    else:
        ciphertext = f.read()
        f.close()
        print("CipherText successfully retrieved")

cipherlen = len(ciphertext)
plainlen = len(plaintext)
keylen = len(key)
#print("Length of the ciphertext is:", cipherlen)
#print("Length of the plaintext is:", plainlen)
#print("Length of the key is:", keylen)

text_index = 0
temp1 = 'a'
temp2 = 'a'
temp3 = 0

if EN:
    f1 = open("CipherText_Result.txt", "w")
    #encryption
    while text_index < plainlen:
        for key_index in range(keylen):
            temp1 = plaintext[text_index]
            temp2 = key[key_index]
            temp3 = ord(temp1) + (ord(temp2)-97)
            if temp3 > 122:
                temp3 = 96 + (temp3 - 122)
            f1.write(chr(temp3))
            text_index += 1
            if text_index >= plainlen:
                break
    print("Encryption completed. The encrypted ciphertext is stored in CipherText_Result.txt")
    f1.close()
else:
    f1 = open("PlainText_Result.txt", "w")
    #decryption
    while text_index < cipherlen:
        for key_index in range(keylen):
            temp1 = ciphertext[text_index]
            temp2 = key[key_index]
            temp3 = ord(temp1) - (ord(temp2)-97)
            if temp3 < 97:
                temp3 = 123 - (97 - temp3)
            f1.write(chr(temp3))
            text_index += 1
            if text_index >= cipherlen:
                break
    print("Decryption completed. The decrypted plaintext is stored in PlainText_Result.txt")
    f1.close()

