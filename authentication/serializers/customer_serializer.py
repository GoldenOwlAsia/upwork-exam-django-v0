from authentication.models import Customer
from rest_framework import serializers
from .profile_serializer import ProfileSerializer


class CustomerSerializer(serializers.ModelSerializer):
    profile_list = ProfileSerializer(read_only=True)
    favorite_profiles = ProfileSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = [
            "id",
            "username",
            "email",
            "password",
            "profile_list",
            "favorite_profiles",
        ]
        extra_kwargs = {"password": {"write_only": True}}
