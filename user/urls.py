from django.urls import path
from user.views import RegisteraAPIView,LoginAPIView,UserView,LogoutAPIView

urlpatterns = [
    path('register',RegisteraAPIView.as_view()),
    path('login',LoginAPIView.as_view()),
    path('user',UserView.as_view()),
    path('logout',LogoutAPIView.as_view()),
    
]
