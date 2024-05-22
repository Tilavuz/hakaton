from rest_framework import serializers
from .models import User, Tuman, Mahalla, Maktab,Viloyat


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "role",
            "rank",
        ]
        extra_kwargs = {"password": {"write_only": True}}

class ViloyatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Viloyat
        fields = "__all__"

class TumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuman
        fields = "__all__"


class MahallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahalla
        fields = "__all__"


class MaktabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maktab
        fields = "__all__"
