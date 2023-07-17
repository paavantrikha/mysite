"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views # Another way to include all views in users app. as user_views is to give our own name to the view. It can be changed.
from django.contrib.auth import views as authentication_views # For authentication. authentication_views is name given by us.
from django.conf import settings
from django.conf.urls.static import static # To upload static files(From server and not database) for eg- profile pictures


urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path('register/', user_views.register, name='register'), #Another way of creating urls
# login/ doesn't take to the desired page after logging in and throws error. For this, add "LOGIN_REDIRECT_URL = 'food:index' " in settings.py
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'), #as_view() is used when using class based views.
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), #login/logout template path is given in template_name as by default, the path is different in django('registration/login.html')
    path('profile/', user_views.profilepage, name='profile'),
]

urlpatterns += [ # To upload static files(From server and not database) for eg- profile pictures

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
