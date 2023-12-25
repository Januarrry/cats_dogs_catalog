# views.py

from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Cat, Dog, Feedback

def feedback(request):
    """
    Renders the feedback form page.

    URL: /catalog/feedback/
    """
    return render(request, "catalog/feedback.html")
    
def index(request):
    """
    Renders the index page with a list of cats and dogs.

    URL: /catalog/
    """
    cat_list = Cat.objects.all()
    dog_list = Dog.objects.all()
    context = {
        "cat_list": cat_list, "dog_list": dog_list
    }
    return render(request, "catalog/index.html", context)

def feedback_success(request):
    """
    Renders the feedback submission success page.

    URL: /catalog/feedback/success/
    """
    return render(request, "catalog/feedback_success.html")

def feedback_submit(request):
    """
    Handles the submission of feedback form.

    URL: /catalog/feedback/submit/
    Method: POST

    Parameters:
        - name: User's name
        - email: User's email address
        - message: Feedback message

    On successful submission, redirects to /catalog/feedback/success/.
    """
    if request.method == 'POST':
        feedback_model = Feedback(
            username=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message'],
            date_sent=timezone.now()
        )
        feedback_model.save()
        return redirect('/catalog/feedback/success')
    else:
        # Handle non-POST requests appropriately
        return redirect('/catalog/feedback/')
