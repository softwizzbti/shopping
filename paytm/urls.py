from django.urls import include, path
from paytm import views


urlpatterns = [
    
    path(r'^$', views.home, name='home'),
    path(r'^payment/', views.payment, name='payment'),
    path(r'^response/', views.response, name='response'),
]
