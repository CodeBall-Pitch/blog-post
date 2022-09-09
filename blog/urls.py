from django.urls import path
from .views import home, about, category_post, allposts, post
app_name = 'blog'
urlpatterns = [
    path('',home,name='home'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about,name = 'about' ),
    path('post/<slug>/', post, name = 'post'),
    path('posts/', allposts, name = 'allposts'),
]