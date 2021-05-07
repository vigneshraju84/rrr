from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from fbv.models import Author
from fbv.serializers import AuthorSerializers


from django.views.decorators.csrf import csrf_exempt


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def author(request):
	
	if request.method == 'GET':
		
		author = Author.objects.all()
		serializer = AuthorSerializers(author, many=True)
		
		return Response(serializer.data)
		
	elif request.method == 'POST':
		#data = JSONParser().parse(request)
		serializer = AuthorSerializers(data=request.data)
		
		if serializer.is_valid():
			
			serializer.save()
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
@csrf_exempt
def author_details(request, pk):
	try:
		author = Author.objects.get(pk=pk)
	except Author.DoesNotExist:
		return HttpResponse(status=404)
		#HTTP_404_NOT_FOUND
		
	if request.method == 'GET':
		serialize_data = AuthorSerializers(author)
		return JsonResponse(serialize_data.data)
		
	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		
		serialize_data = AuthorSerializers(author, data=data)
		
		if serialize_data.is_valid():
			serialize_data.save()
			
			return JsonResponse(serialize_data.data)
			
		return JsonResponse(serialize_data.errors, status=400)
		
	
	elif request.method == 'DELETE':
		author.delete()
		return JsonResponse(status=204)
		#HTTP_204_NO_CONTENT
		#HTTP_200_OK
		
		