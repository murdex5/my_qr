from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time
# Create your views here.

def qr_gen(request):
    if request.method == 'POST':
        data = request.POST['data']
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(settings.MEDIA_ROOT + '/' + img_name)
        context = {
            'img_name': img_name
            }
        return render(request, 'index.html', context)
    return render(request, 'index.html')