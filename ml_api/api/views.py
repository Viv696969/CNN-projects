from django.shortcuts import render
from .models import *
from .ml_loader import predict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.
import os
import shutil

@csrf_exempt
def predict_brain_tumor(request):
    if request.method=='POST':
        image=Image.objects.create(image=request.FILES['brainimage'])
        print(image.image.name)
        img_path='./media/'+image.image.name
        print(f'image_path={img_path}')
        results=predict(img_path)
        image.delete()
        # os.remove(img_path)
        try:
            dest=f'./media/images/brain{results[0]}'
            shutil.move(src=img_path,dst=dest)
        except:
            return JsonResponse({'mssg':"predicted but unabel to move"})

        return JsonResponse({'mssg':'image predicted + moved by shutil  successfully'})

