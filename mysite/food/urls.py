from . import views
from django.urls import path

app_name = 'food' # app name is mentioned so that if there is another url pattern with same name in a different app, django knows which app to route to

urlpatterns = [
    # /food/
    path('', views.index, name='index'),
    # /food/1 where 1,2,3 etc are food id
    path('<int:item_id>/', views.detail, name='detail'), # To pass integer
    path('item/', views.item, name='item'),
]