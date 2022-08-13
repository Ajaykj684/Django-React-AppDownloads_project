from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialize import AccountSerializer,AppSerializer,ProfileSerializer,TaskSerializer
from rest_framework.decorators import api_view
from .models import Account , Profile , Task , App
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
    print("loookkk")

@api_view(['GET','POST'])

def getRoutes(request):
    routes =[
        '/api/token',
        '/api/token/refresh',
       

        ]
    return Response(routes)



class Home(APIView):
    def get(self ,request):
        return HttpResponse("<h1>its home</h1>")

class Login(APIView):
    def post(self,request):
        
        body = request.body.decode('utf-8')
        body = json.loads(body)
        username = body['username']
        password = body['password']
        user = auth.authenticate(email=username, password=password)
       
        if user is not None :
          
           obj=AccountSerializer(user)
           return Response (obj.data)
        else :
            return Response(status=400)
            


class Register(APIView):
    def post(self,request):
        body = request.body.decode('utf-8')
        body = json.loads(body)
        firstname = body['firstName']
        lastname = body['lastName']
        email = body['email']
        password = body['password']
        Account.objects.create(email=email, password=password, first_name = firstname , last_name = lastname , username= email)
       
        return Response (200)


           
class AppDownload(APIView):
    def post(self,request,id,userId):
        user= Account.objects.get(id = userId)
        app = App.objects.get(id=id)
        
        Task.objects.create(User=user, Appname = app.Appname , Point = app.Point, AppId = app.id)
        newPoint =  user.Point + app.Point
        taskCompleted = user.Task + 1
        currentuser= Account.objects.filter(id = userId)
        currentuser.update(Point = newPoint, Task = taskCompleted )

        task =  Task.objects.filter(User=user)
        obj = TaskSerializer(task,many=True)

        return Response (obj.data)




class TaskCompleted(APIView):
    def get(self,request,id):
        user= Account.objects.get(id = id)

        task =  Task.objects.filter(User=user)
     
        obj = TaskSerializer(task,many=True)
        print(obj.data,"ajayyy loook")
        return Response (obj.data)



class UserDetails(APIView):
    def get(self,request,id):
        user= Account.objects.get(id = id)
        obj = AccountSerializer(user)
        return Response (obj.data)





class TaskDetails(APIView):
    def get(self,request,id):

        app =  App.objects.get(id=id)
        obj = AppSerializer(app)
        return Response (obj.data)
