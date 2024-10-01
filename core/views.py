from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Appeal
from .serializers import AppealModelSerializer

class CreateAppeal(APIView):
    def post(self, request):
        ser = AppealModelSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.create(ser.validated_data)
        return Response(status=200)
    
class AppealsList(APIView):
    def get(self, request):
        return Response( AppealModelSerializer(Appeal.objects.all(), many=True).data)
        
    
    
    


# Create your views here.
