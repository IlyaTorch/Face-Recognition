from django.shortcuts import render, redirect
from .models import Url, BoundingBox
import cv2
from imutils import url_to_image 

face_cascade = cv2.CascadeClassifier('/haarcascade_frontalface_default.xml')


def index(request):
    if request.method == 'POST':

        url = Url.objects.create(image_url=request.POST.get('image_url'))
        url.save()

        img = url_to_image(request.POST.get('image_url'))
        ih, iw, _ = img.shape

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            top = round(y * 100 / ih, 2)
            right = round((iw - x - w) * 100 / iw, 2)
            left = round(x * 100 / iw, 2)
            bottom = round((ih - y - h) * 100 / ih, 2)
            bounding_box = BoundingBox.objects.create(top=top,
                                                      right=right,
                                                      left=left,
                                                      bottom=bottom,
                                                      image=url)
            bounding_box.save()
            
        return redirect('/face')

    image_urls = Url.objects.all()

    context = {'image_urls': image_urls}
    return render(request, 'face/index.html', context=context)


def delete(request, url_id):
    item = Url.objects.get(pk=url_id)
    item.delete()
    return redirect('/face')