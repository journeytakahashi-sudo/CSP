#   a212_rsa_decrypt.py
import rsa as rsa
import read_file as rf

key = int(input("Enter the Decryption Key: " ))
mod_value = int(input("Enter the Modulus: " ))
encrypted_msg = input("What message would you like to decrypt? \t Paste it OR type 'file' : \n")

if (encrypted_msg == "file"):
    filename = "input_message"
    print("Ok, reading input message from file '" + filename + "'")
    plaintext = rf.get_file_firstline(filename)
else:
    plaintext = encrypted_msg.split(", ") #create list from input string
    
print("\n" + rsa.decrypt(key,mod_value, plaintext), end="\n\n")
