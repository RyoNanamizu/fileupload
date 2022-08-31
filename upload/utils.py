import datetime
import time
from cryptography.fernet import Fernet
from django.core.files.uploadedfile import UploadedFile

#get file by js
def handle_uploaded_file_js(f:UploadedFile):
    filename = f.name
    
    with open(f'/tmp/{filename}', 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# get file by form
def handle_uploaded_file(f:UploadedFile):
    # key generation
    key = Fernet.generate_key()
    fernet = Fernet(key)

    # make fake key
    index = key.find(b'=')
    fake_key_str = key[1:index].decode() + key[0:1].decode() + key[index:].decode()
    
    filename = get_new_filename(f.name, key)
    
    with open(f'/tmp/{filename}', 'wb') as destination:
        destination.write((f'>{fake_key_str}<\n').encode())
        for chunk in f.chunks():
            payload = fernet.encrypt(chunk)
            destination.write(payload)
            destination.write('\n'.encode())
            
            
def get_new_filename(filename:str, key:bytes) -> str:
    ext_index = filename.rfind('.')
    ext = filename[ext_index+1:]
    
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    
    timestamp = time.time()
    
    k = key[1:6].decode()
    
    return f'{today}_{timestamp}_{k}.{ext}'