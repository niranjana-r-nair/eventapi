from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from accounts.models import MyUser
from accounts.serializers import UserSerializer
class RegisterAPI(viewsets.ModelViewSet):
    queryset=MyUser.objects.all()
    serializer_class=UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
class LogoutAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':'deleted'},status=status.HTTP_200_OK)
