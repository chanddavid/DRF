from django.shortcuts import render
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
import io
from rest_framework import status


# Create your views here.
class get_api(APIView):
    def get(self, request,id=None):
        if id is not None:
            innerdata = Student.objects.get(id=id)
            serializer = StudentSerializer(innerdata)
            print(serializer.data)
            
        else:   
            innerdata = Student.objects.all()
            serializer = StudentSerializer(innerdata, many=True)
            print(serializer.data)

        return Response(
            {"msg": "successfully listed", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"data": "successfully created", "value": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors)

    def put(self, request,id):
        innerdata = Student.objects.get(id=id)
        serializer = StudentSerializer(innerdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg": "successfully updated", "data": serializer.data},
                status=status.HTTP_202_ACCEPTED,
            )
        else:
            return Response(serializer.errors)

    def patch(self, request,id):

        innerdata = Student.objects.get(id=id)
        serializer = StudentSerializer(innerdata, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg": "successfully partial updated", "data": serializer.data},
                status=status.HTTP_202_ACCEPTED,
            )
        else:
            return Response(serializer.errors)


    def delete(self, request,id):
        innerdata = Student.objects.get(id=id)
        innerdata.delete()
        return Response(
            {"msg": "successfully deleted"},
            status=status.HTTP_200_OK,
        )

