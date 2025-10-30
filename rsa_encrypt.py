#   a212_rsa_encrypt.py
import rsa as rsa
import read_file as rf

key = int(input("Enter the Encryption Key: " ))
mod_value = int(input("Enter the Modulus: " ))
plaintext = input("Enter a message to encrypt OR type 'file'\n")

if (plaintext == "file"):
    filename = "input_message"
    print("Ok, reading input message from file '" + filename + "'")
    plaintext = ", ".join(rf.get_file_firstline(filename))
encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
    
print("Encrypted Message:\n")
print(*encrypted_msg, sep=", ", end="\n\n") #Print without brackets
