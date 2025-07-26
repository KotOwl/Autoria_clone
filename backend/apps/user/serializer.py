from django.contrib.auth import get_user_model
from django.db.transaction import atomic
from rest_framework import serializers


from apps.user.models import ProfileModel
from core.services.email_service import EmailService
from core.services.jwt_service import JWTService

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'is_staff',
                  'is_active', 'is_superuser',
                  'password', 'last_login', 'profile',
                  'created_at', 'updated_at',)
        read_only_fields = ('id', 'is_staff', 'is_active', 'is_superuser', 'created_at', 'updated_at', 'last_login',
                            "is_active",
                            "is_seller",
                            "is_buyer", "account_type",)

        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }
    @atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        EmailService.register(user)
        return user
