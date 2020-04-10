from django.contrib import admin
from .models import Job
from jobs.models import User
from jobs.models import Product
from jobs.models import Feedback


# feedback

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Feedback)

# feedback #

admin.site.register(Job)
