from django.urls import path

from users.views import UserSignupApiView

urlpatterns = [
    # register new user by API
    path('api/signup/', UserSignupApiView.as_view(), name='user_signup'),
]
