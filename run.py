import base64
import time
import hashlib
print("""
███╗░░██╗░░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
████╗░██║░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██╔██╗██║█████╗██║░░╚═╝██║░░██║██║░░██║█████╗░░██████╔╝
██║╚████║╚════╝██║░░██╗██║░░██║██║░░██║██╔══╝░░██╔══██╗
██║░╚███║░░░░░░╚█████╔╝╚█████╔╝██████╔╝███████╗██║░░██║
╚═╝░░╚══╝░░░░░░░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝""")
print("__________________________________________")
time.sleep(2)
print("           CREATED BY  >> LORD xRO OF CEO")
time.sleep(2)
print("           THANKS  TO  >> ALL CEO MEMBERS")
time.sleep(2)
print("           RECORD  BY  >> THE TERMUX ACADEMY")
print("__________________________________________")
string = input("Enter your text >>")
in_bytes = string.encode("ascii")
base64 = base64.b64encode(in_bytes)
b64_string = base64.decode("ascii")
res = ''.join(format(ord(x), '08b') for x in string)
hex = string.encode("utf-8").hex()
hash_object = hashlib.md5(string.encode())
md5_hash = hash_object.hexdigest()
print('Please Wait while processing..........')
time.sleep(2)
print("THE HEX CODE IS    >> "+b64_string)
print("THE BINARY CODE IS >> "+res)
print("THE OCTAL CODE IS  >> "+hex)
print("THE HASH CODE IS   >> "+md5_hash)
