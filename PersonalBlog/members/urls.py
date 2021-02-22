from django.urls import path
from .views import UserRegisterView

# register sayfasına bu sayfadan farklı fieldler ekleyebiliriz
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
]
