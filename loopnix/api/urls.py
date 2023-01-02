from loopnix.api.views import RegistrationView,ChangePasswordView,UserListView,DeleteUserView,UpdateProfileView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/',RegistrationView.as_view(),name='register'),
    path('users/',UserListView.as_view(),name='user-list'),
    path('delete/<int:pk>/',DeleteUserView.as_view(),name='delete-user'),
    path('update/<int:pk>/',UpdateProfileView.as_view(),name='update-user'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
]