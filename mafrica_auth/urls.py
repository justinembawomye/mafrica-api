from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, current_user, UserAPI, Logout


urlpatterns = [
    path('signup/', RegistrationAPIView.as_view(), name='user_registration'),
    path('login/', LoginAPIView.as_view(), name='user_login'),
      path('user/', UserAPI.as_view()),
     path('current_user/', current_user),
     path('logout/', Logout.as_view()),
]