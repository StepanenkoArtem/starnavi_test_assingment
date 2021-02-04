from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from users.models import SocialUser
from users.serializers import RegisterSerializer


class UserSignupApiView(CreateAPIView):
    queryset = SocialUser.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer
