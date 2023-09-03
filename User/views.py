from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from RestApi import serializer
from RestApi.serializer import CustomUserSerializer


class CreateUser(APIView):
    """handle creating and updating profiles"""
    # permission_classes = [IsAdminUser]
    def post(self, request):
        if request.method == 'POST':
            serializers = CustomUserSerializer(data=request.data)
            if serializers.is_valid():
                user = serializers.save()
                # print('response:' + str(serializers.data))
                return Response({'message': 'کاربر با موفقیت ثبت گردید .', 'data': serializers.data})

        return Response({'message': 'خطا', 'error': serializers.errors, 'status': status.HTTP_400_BAD_REQUEST})


class UpdateUser(APIView):
    def patch(self,request):
        userId = request.data.get('id')
        item = serializer.CustomUser.objects.filter(id=userId).first()
        if request.method == 'PATCH':
            serialize_r = CustomUserSerializer(item, data=request.data, partial=True)
            if serialize_r.is_valid():
                serialize_r.save()
                firstName = request.data.get('first_name')
                lastName = request.data.get('last_name')
                if lastName == None:
                    print('lastName is Null')

                return Response({'message': 'ok', 'data': serialize_r.data,
                                 'status': status.HTTP_200_OK})
            return Response({'message': 'fail ', 'error': serialize_r.errors,
                             'status': status.HTTP_400_BAD_REQUEST})