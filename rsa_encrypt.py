#   a212_rsa_encrypt.py
import rsa as rsa

key = int(input("Enter the Encryption Key: " ))
mod_value = int(input("Enter the Modulus: " ))
plaintext = input("Enter a message to encrypt: ")
encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
print("Encrypted Message:\n")
print(*encrypted_msg, sep=", ", end="\n\n") #Print without brackets
