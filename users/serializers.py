from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import SocialUser


class RegisterSerializer(serializers.ModelSerializer):
    users = SocialUser.objects.all()
    email = serializers.EmailField(
        validators=[UniqueValidator(users, message='Email already registered')],
    )
    password = serializers.CharField(required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = SocialUser
        fields = (
            'email',
            'password',
            'last_name',
            'first_name',
        )

    def create(self, validated_data):
        user = SocialUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
