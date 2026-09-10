
from rest_framework import serializers
from accounts.models import MyUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=['username','password','email','role','phone']


    def create(self,validated_data):
        return MyUser.objects.create_user(**validated_data)