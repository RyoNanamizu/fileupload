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
    

def  upload(request):
    if request.method=='GET':
        return render(request,'upload/upload.html', {"pub": settings.PUBLIC_KEY})
    elif request.method=='POST':
        data = request.POST.get('data')
        print(type(data))
        print(data.encode('utf-8'))
        key_obj = request.FILES.get('key')
        file_obj = request.FILES.get('file')
        print(len(key_obj))
        print(len(file_obj))
        # file_name = 'test'
        # 拼接绝对路径
        # file_path = os.path.join('/tmp', file_name)
        # with open(file_path, 'wb') as f:
            
        #     for chunk in file_obj.chunks():#chunks()每次读取数据默认我64k
        #         f.write(chunk)
        return HttpResponseRedirect("/success")
    