from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class Productcurd(APIView):
    
    def get(self,request):
        PQS=Product.objects.all()
        pjd=Productserializer(PQS,many=True)
        return Response(pjd.data)
    
    
    def post(self,request):
        PMSD=Productserializer(data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'message':'Product is created'})
        return Response({'Failed':'Product is not created'})
    
    
    def put(self,request):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=Productserializer(PO,data=request.data)
        if UPO.is_valid:
            UPO.save()
            return Response({'message':'product is created'})
        return Response({'failed':'Product is not created'})