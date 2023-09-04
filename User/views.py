from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from RestApi import serializer
from RestApi.serializer import CustomUserSerializer
import jwt, datetime


class CreateUser(APIView):
    """handle creating and updating profiles"""

    # permission_classes = [IsAdminUser]
    def post(self, request):
        if request.method == 'POST':
            serializers = CustomUserSerializer(data=request.data)
            if serializers.is_valid(raise_exception=True):
                user = serializers.save()
                # print('response:' + str(serializers.data))
                return Response({'message': 'کاربر با موفقیت ثبت گردید .', 'data': serializers.data})

        return Response({'message': 'خطا', 'error': serializers.errors, 'status': status.HTTP_400_BAD_REQUEST})


class UpdateUser(APIView):
    def patch(self, request):
        userId = request.data.get('id')
        item = serializer.CustomUser.objects.filter(id=userId).first()
        if request.method == 'PATCH':
            serialize_r = CustomUserSerializer(item, data=request.data, partial=True)
            if serialize_r.is_valid(raise_exception=True):
                serialize_r.save()
                firstName = request.data.get('first_name')
                lastName = request.data.get('last_name')
                if lastName == None:
                    print('lastName is Null')

                return Response({'message': 'ok', 'data': serialize_r.data,
                                 'status': status.HTTP_200_OK})
            return Response({'message': 'fail ', 'error': serialize_r.errors,
                             'status': status.HTTP_400_BAD_REQUEST})


class UserDetails(APIView):
    def get(self, request):
        response = Response()
        userId = request.data.get('id')
        token = request.data.get('token')
        print('token= '+token)
        item = serializer.CustomUser.objects.filter(id=userId).first()
        serialize_r = serializer.CustomUserSerializer(item)
        response.data = {
            'message': 'user found successfully',
            'status': status.HTTP_200_OK,
            'data': serialize_r.data
        }
        return response


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = serializer.CustomUser.objects.filter(username=username).first()

        print(user)
        if user is None:
            return Response({'message': 'User not found', 'status': status.HTTP_404_NOT_FOUND})
        if not user.check_password(password):
            return Response({'message': 'Username or Password is incorrect', 'status': status.HTTP_403_FORBIDDEN})

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secretHSA@%^DSGAGASERWHTRJYHHERYREYH', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'token': token,
            'message': 'User Logged in successfully',
            'status': status.HTTP_200_OK

        }
        return response
