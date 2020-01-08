from django.contrib import admin
from django.urls import path
from .views import (Sendmail, user_form)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_form),
    path('sendmail/', Sendmail)
]