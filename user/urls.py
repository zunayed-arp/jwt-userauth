from django.urls import path
from user.views import Register

urlpatterns = [
    path('register',RegisterAPIView.as_view())
]
