from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from User.models import CustomUser


class CreateUser(APIView):
    """handle creating and updating profiles"""
    permission_classes = [IsAdminUser]

    def post(self, request):
        if request.method == 'POST':
            serializer_s = CustomUser(data=request.data)
            if serializer_s.is_valid():
                user = serializer_s.save()
                return Response(
                    {'message': 'کاربر با موفقیت ثبت گردید .', 'data': serializer_s.data})
        return Response({'message': 'خطا', 'error': serializer_s.errors, 'status': status.HTTP_400_BAD_REQUEST})
