# Hiya Jain
# Lab 03: Brute Force Decryption
# CISC 1800 - Introduction to Computer Programming

def decrypt_caesar (message):
    for key in range (26):
        translated = []
        for ch in message:
            if ch.isalpha():
                num = ord(ch)-1
                num -= key
                if num < 0:
                    num += 26
                if ch.islower():
                    translated.append(chr(num + ord('a')))
                else:
                    translated.append(chr(num + ord('A')))
            else:
                translated.append(ch)
        decrypted_message = "".join(translated)
        filename = f'decrypted_message_{key}.txt'
        with open(filename, 'w') as f:
            f.write(decrypted_message)
    return (translated)

def retrieve_data(file_name):
    with open (file_name, "r") as f:
        data = f.read()
        return data
      
def main ():
    intercepted_comm_file = "intercepted_comm00.txt"
    data = retrieve_data(intercepted_comm_file)
    decrypt_caesar(data)
  
main ()
