#   a212_rsa_encrypt.py
import rsa as rsa
import read_file as rf

"""
Produce a private-key encrypted "certificate" for each "name,student-key,modulus" row in filename,
for students to decode using the Certificate Authority's public key.

1. Paste columns from spreadsheet (name, public key, modulus) into input_message
2. Run this program -- encrypts all rows using hard-coded private key and modulus
3. Values are reversible with paired public key
"""

def get_student_keys(filename):
    all_line_lists = []
    try:
        with open(filename, "r") as file:
            for line in file: 
                lineList = line.strip().split()
                # print(lineList)
                all_line_lists.append(lineList)
    except FileNotFoundError:
        print("Error: The file '" + filename + "' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    return all_line_lists

studentCert_details = (get_student_keys("input_message"))

for studentCert in studentCert_details:
    studentName = studentCert[0]
    plaintext = ", ".join(studentCert)
    CAprivK = 2 * 19 * 211 - 1
    CAmod = 26123
    #CA public key: 14353
    encrypted_msg = rsa.encrypt(CAprivK, CAmod, plaintext) 
    # print(studentName)
    print(*encrypted_msg, sep=", ", end="\n")

