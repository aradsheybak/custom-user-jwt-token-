from django.urls import path
from User.views import CreateUser, UpdateUser, UserDetails,Login
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('user/register/', CreateUser.as_view()),
    path('user/update/', UpdateUser.as_view()),
    path('user/details/', UserDetails.as_view()),
    path('user/login/', Login.as_view()),

]
