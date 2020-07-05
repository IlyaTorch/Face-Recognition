from django.shortcuts import render
from .models import Url


def index(request):
    if request.method == 'POST':

        url = Url.objects.create(image_url=request.POST.get('image_url'))
        url.save()

    image_urls = Url.objects.all()

    context = {'data': image_urls}
    return render(request, 'face/index.html', context=context)
