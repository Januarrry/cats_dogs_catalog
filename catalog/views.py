from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Cat, Dog, Feedback
def feedback(request):
    return render(request, "catalog/feedback.html")
    
def index(request):
    cat_list = Cat.objects.all()
    dog_list = Dog.objects.all()
    context = {
        "cat_list": cat_list, "dog_list": dog_list
    }
    return render(request, "catalog/index.html", context)

def feedback_success(request):\
    return render(request, "catalog/feedback_success.html")

def feedback_submit(request):
    print(request.POST)
    feedback_model = Feedback(username = request.POST['name'], 
                              email = request.POST['email'], 
                              message = request.POST['message'],
                              date_sent = timezone.now())
    feedback_model.save()
    return redirect('/catalog/feedback/success')