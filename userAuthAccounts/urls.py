from django.urls import path
from .views import home, loginUser, registerUser, logoutUser

urlpatterns = [
    # class based views
    path('', home.as_view(), name='home'),
    path('login/', loginUser.as_view(), name='user_login'),
    path('register/', registerUser.as_view(), name='user_register'),
    path('logout/', logoutUser.as_view(), name='user_logout'),
]