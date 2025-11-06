
def get_file_firstline(filename):
    """
    Reads first line from specified file and returns it as a list.
    
    !!! Expects first line to be the output from rsa_encrypt or rsa_decrypt !!!
    
    Args:
        filename: file containing **only the output from rsa_encrypt or rsa_decrypt**
    Returns:
        list: A list representing the numbers in the top line of the file
    """
    try:
        with open(filename, "r") as file:
            # Read the first line:
            line = file.readline()
            # Remove the newline character and split the line into a list:
            line_as_list = line.strip().split(", ")
            return line_as_list
    except FileNotFoundError:
        print("Error: The file '" + filename + "' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
