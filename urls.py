from django.contrib import admin
from django.urls import path
from nse.views import index, show_result

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('result/', show_result, name='show_result'),
]
