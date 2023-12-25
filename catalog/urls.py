from django.urls import path

from . import views

app_name = "catalog"
urlpatterns = [
    path("", views.index, name="index"),
    path("feedback/", views.feedback, name="feedback"),
    path("feedback/submit", views.feedback_submit, name="feedback_submit"),
    path("feedback/success", views.feedback_success, name="feedback_success"),
]