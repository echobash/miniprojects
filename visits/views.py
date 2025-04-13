from django.shortcuts import render
from .models import Visit


def home(request):
    v = Visit.objects.first()
    v.count += 1
    v.save()
    context = {
        'count': v.count
    }
    return render(request, 'home.html', context=context)
