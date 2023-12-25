from django.shortcuts import render

from .models import Cat, Dog
def index(request):
    cat_list = Cat.objects.all()
    dog_list = Dog.objects.all()
    context = {
        "cat_list": cat_list, "dog_list": dog_list
    }
    return render(request, "catalog/index.html", context)

