from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

__all__ = [
    "EmailSerializer",
    "PasswordTokenSerializer",
    "TokenSerializer",
]


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordTokenSerializer(serializers.Serializer):
    password = serializers.CharField(
        label=_("Password"), style={"input_type": "password"}
    )
    token = serializers.CharField()
    register = serializers.BooleanField()


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()
    register = serializers.BooleanField()
