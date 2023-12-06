#Script to unencrypt
from Crypto.Cipher import AES

key = b'\xec[V\xd5\xa5U\xfa\xbe[c\xc2\xd0\xe9gYT' #Get this from the encrypt file

file_in = open("encrypted.bin", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
file_in.close()

# let's assume that the key is somehow available again
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data)