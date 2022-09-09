from django.contrib import admin
from  .models import Author, Category, Post
# Register your models here.
admin.site.site_header = "Kiash Blog  Admin"
admin.site.site_title = "Kiash Blog Admin Portal"
admin.site.index_title = "Welcome to Kiash Blog Portal"



admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)