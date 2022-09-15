from django.contrib import admin
from .models import User, Profile
# Register your models here

admin.site.site_header = 'kiash Blog Admin Panel'
admin.site.site_title = 'kiash Blog Admin Panel'
admin.site.index_title = 'kiash Blog Admin Panel'

admin.site.register(User)
admin.site.register(Profile)