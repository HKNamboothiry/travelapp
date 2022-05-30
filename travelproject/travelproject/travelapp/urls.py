from django.urls import path, include

from travelapp import views

urlpatterns = [
    path('', views.helloWorld, name='HelloWorld'),
    path('register/', views.register, name='Register'),
    #I've given the path for the login and logout pages below and for the register function above...
    path('login',views.login, name='login'),
    path('logout',views.logout,name='logout')
    # path('about/', views.about, name='about')
]