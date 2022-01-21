from django.urls import path
from user.views import RegisteraAPIView,LoginAPIView

urlpatterns = [
    path('register',RegisteraAPIView.as_view()),
    path('login',LoginAPIView.as_view()),
]
