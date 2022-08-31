import random
import os
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from .forms import UploadFileForm
from .utils import handle_uploaded_file, handle_uploaded_file_js


def success(request):
    return render(request, 'upload/success.html')


# Imaginary function to handle an uploaded file.
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect("/success")
#     else:
#         form = UploadFileForm()
#         i = random.randint(1,3)
#         return render(request, f'upload/upload{i}.html', {'form': form})
    

def  upload(request):
    if request.method=='GET':
        return render(request,'upload/upload.html')
    elif request.method=='POST':
        file_obj = request.FILES.get('file')
        file_name = file_obj.name
        # 拼接绝对路径
        file_path = os.path.join('/tmp', file_name)
        with open(file_path, 'wb')as f:
            for chunk in file_obj.chunks():#chunks()每次读取数据默认我64k
                f.write(chunk)
        return HttpResponseRedirect("/success")
    