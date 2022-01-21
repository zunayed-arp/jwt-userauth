from rest_framework.views import APIView
from user.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from user.models import User
import jwt,datetime



class RegisteraAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def get(self,request):
        data = User.objects.all()
        serializer = UserSerializer(data,many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    

class LoginAPIView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        
        
        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('User not Found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        
        
        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload,'secret', algorithm='HS256').decode('utf-8')
        
        response = Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={
            'jwt':token
        }
        return response
        
        
        
            
            
