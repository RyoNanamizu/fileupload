from datetime import datetime
import random
import time
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from cryptography.fernet import Fernet


def success(request):
    i = random.randint(1,3)
    # return HttpResponseRedirect("/success")
    return render(request, f'upload/success{i}.html')


# Imaginary function to handle an uploaded file.
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect("/success")
    else:
        form = UploadFileForm()
        i = random.randint(1,3)
        return render(request, f'upload/upload{i}.html', {'form': form})
        

def handle_uploaded_file(f):
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
    
    today = datetime.today().strftime('%Y-%m-%d')
    
    timestamp = time.time()
    
    k = key[1:6].decode()
    
    return f'{today}_{timestamp}_{k}.{ext}'
    