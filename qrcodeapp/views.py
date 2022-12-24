# qrcodeapp/views.py

from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time

def qr_gen(request):
    if request.method == 'POST':
        data = request.POST['data']
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        path = settings.MEDIA_ROOT
        img.save( str(path) + '/' + img_name)
        return render(request, 'index.html', {'img_name': img_name})
    return render(request, 'index.html')