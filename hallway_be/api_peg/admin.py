from django.contrib import admin
# Register your models here.
from .models import goalPeg

from django.contrib import admin

# Register your models here.
# it allows to have a user friendly interface to input data in the db
admin.site.register(goalPeg)