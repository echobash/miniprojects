from django.shortcuts import render
from .models import Visit


def home(request):
    v, created = Visit.objects.get_or_create(id=1)
    v.count += 1
    v.save()
    context = {
        'count': v.count
    }
    return render(request, 'home.html', context=context)
