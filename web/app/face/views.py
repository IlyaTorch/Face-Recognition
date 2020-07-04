from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        print(request.POST.get('image_url'))
    context = {'data': 'face app'}
    return render(request, 'face/index.html', context=context)
