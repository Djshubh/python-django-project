from django.shortcuts import render
from .models import Destination
# for rest api call --- 

from django.http import HttpResponse 
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import destSerializer
# from .models import Destination                  ## already imported

# Create your views here.
def index(request):
    
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests':dests})
    #return render(request, "index.html", {'price':700})

class destList(APIView):

    def get(self, request):
        dest1 = Destination.objects.all()
        serializer = destSerializer(dest1,many = True)

        return Response(serializer.data)

    def post(self,request):
        pass