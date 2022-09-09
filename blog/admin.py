from django.contrib import admin

# Register your models here.
admin.site.site_header = "Kiash Blog  Admin"
admin.site.site_title = "Kiash Blog Admin Portal"
admin.site.index_title = "Welcome to Kiash Blog Portal"


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title','slug','author','created_on','status')
#     list_filter = ("status",)
#     search_fields = ['title', 'content']
