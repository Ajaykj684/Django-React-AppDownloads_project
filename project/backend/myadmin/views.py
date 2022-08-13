from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serialize import AccountSerializer,AppSerializer,ProfileSerializer,TaskSerializer
from rest_framework.decorators import api_view
from user.models import Account , Profile , Task , App
from rest_framework import status
import json
from django.contrib import messages,auth
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        
        token = super().get_token(user)

        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET','POST'])

def getRoutes(request):
    routes =[
        '/api/token',
        '/api/token/refresh',
       

        ]
    return Response(routes)



class Myadmin(APIView):
    def post(self, request):
        pass
    
    def get(self , request):
        data =  App.objects.all()
        obj = AppSerializer(data,many=True)
        return Response(obj.data)



class AdminLogin(APIView):
    def post(self,request):
        body = request.body.decode('utf-8')
        body = json.loads(body)
        username = body['username']
        password = body['password']
        user = auth.authenticate(email=username, password=password)
        
       
        if user is not None and user.is_admin == True :
           obj=AccountSerializer(user)
           return Response (obj.data)
        else :
            return Response(status=400)



class AddApp(APIView):
    def post(self,request):
        body = request.body.decode('utf-8')
        body = json.loads(body)
        Appname = body['Appname']
        Applink = body['Applink']
        Point = body['Point']

        App.objects.create(Applink=Applink, Appname=Appname, Category="Games", SubCategory="Music" ,Point=Point)
       
        return Response (200)
       




class DeleteApp(APIView):
    def post(self,request,id):
        app = App.objects.filter(id =id)
        app.delete()
        Apps =  App.objects.all()
        obj = AppSerializer(Apps,many=True)
        return Response (obj.data)
       


