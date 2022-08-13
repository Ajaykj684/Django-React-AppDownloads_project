from dataclasses import field
from rest_framework import serializers
from user.models import Account , Task , Profile ,App





class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields="__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model=App
        fields="__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields="__all__"