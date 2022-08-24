from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()
fernet = Fernet(key)

index = key.find(b'=')
fake_key_str = key[1:index].decode() + key[0:1].decode() + key[index:].decode()
print(key)
print(fake_key_str)

# opening the original file to encrypt
with open('./test.txt', 'rb') as file, open('./encrypt.txt', 'wb') as encrypted_file:
    encrypted_file.write((f'>{fake_key_str}<\n').encode())
    for line in file.readlines():
        encrypted = fernet.encrypt(line)
        encrypted_file.write(encrypted)
        encrypted_file.write('\n'.encode())
        
# # key generation
# key = Fernet.generate_key()
 
# # string the key in a file
# with open('filekey.key', 'wb') as filekey:
#    filekey.write(key)
   
# with open('filekey.key', 'rb') as filekey:
#     key = filekey.read()
#     index = key.find(b'=')
#     fake_key_str = key[1:index].decode() + key[0:1].decode() + key[index:].decode()

# # using the generated key
# fernet = Fernet(key)
 
# tmp =[]
# # opening the original file to encrypt
# with open('./test.txt', 'rb') as file:
#     for line in file.readlines():
#         tmp.append(line)

# en = []
# en.append((f'>{fake_key_str}<\n').encode())

# for t in tmp:
#     # encrypting the file
#     encrypted = fernet.encrypt(t)
#     en.append(encrypted)
#     en.append('\n'.encode())
    
# # opening the file in write mode and
# # writing the encrypted data
# with open('./encrypt.txt', 'wb') as encrypted_file:
#     for e in en:
#         encrypted_file.write(e)