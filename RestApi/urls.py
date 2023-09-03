from django.urls import path
from User.views import CreateUser,UpdateUser
urlpatterns = [
    path('users/register/', CreateUser.as_view()),
    path('users/update/', UpdateUser.as_view()),

]
