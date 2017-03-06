#python
import json

#Django Core
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

#Rest Framework
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes

@api_view(['POST'])
@parser_classes((FormParser, MultiPartParser))
def search(request):
    if request.method == 'GET':
        return HttpResponse("Hello from search")
    elif request.method == 'POST':
        parser_classes = (MultiPartParser, FormParser,)
        title = request.data.get('title')
        image = request.FILES['file']
        filename = 'myfile'
        with open(filename, 'wb+') as temp_file:
            for chunk in image.chunks():
                temp_file.write(chunk)

        my_saved_file = open(filename)
        return Response("Got image " + title)
