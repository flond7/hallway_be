from django.contrib import admin

# Register your models here.
from .models import customUser, askUser, PAUser, PAOffice, PACredentials, officeMail, officeSDI, userLan #, officeAdweb, userAdweb,userEmail,

from django.contrib import admin

# Register your models here.
# it allows to have a user friendly interface to input data in the db

#admin.site.register(User)
admin.site.register(customUser)
admin.site.register(askUser)
admin.site.register(PAUser)
admin.site.register(PAOffice)
admin.site.register(PACredentials)

