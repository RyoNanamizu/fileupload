from cryptography.fernet import Fernet
    
lines = []
with open('/tmp/2022-08-24_1661371044.2608037_x_X1b.dmg', 'rb') as encrypted_file, open('./de', 'wb') as decrypt_file:
    key = b''
    for line in encrypted_file.readlines():
        if b'<\n' in line:
            tmp_key = line.replace(b'>', b'').replace(b'<\n', b'')
            index = tmp_key.find(b'=')            
            key = tmp_key[index-1:index].decode() + tmp_key[0:index-1].decode() + tmp_key[index:].decode()
            fernet = Fernet(key)            
        else:
            payload = fernet.decrypt(line)
            decrypt_file.write(payload)