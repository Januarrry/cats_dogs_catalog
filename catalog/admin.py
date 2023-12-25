from django.contrib import admin

from .models import Cat, Dog, Feedback
admin.site.register(Cat)
admin.site.register(Dog)
admin.site.register(Feedback)
