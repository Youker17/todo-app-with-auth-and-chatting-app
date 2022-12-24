from django.urls import path , include
from . import views
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path("register/", views.register , name="register"),
    path('login/', views.login_user),
    path("logout/", LogoutView.as_view()),
    path('profile/', views.profile)
]
