# These are 2 files combined here 
# First one is of app (url.py)
# Second one is of project (url.py)

# First One
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('youtubevideodownloader/', views.youtube),
]


# Second One
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', include('first.urls')),
]
