from django.shortcuts import render
from .models import Books
from .serializer import BooksSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class BookAPIView(APIView):
	def get(self, request):
		book = Books.objects.all()
		serializer = BooksSerializer(book, many=True)
		return Response(serializer.data)
	def post(self, request):
		serializer = BooksSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()	
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		
	def get_object(self, id):
		try:
			return Books.objects.get(pk=id)
		except Books.DoesNotExits:
			return HttpResponse(status = status.HTTP_404_NOT_FOUND)
	def get(self, request, id):
		book = self.get_object(id)
		serializer = BooksSerializer(book)
		return Response(serializer.data)
	def put(self, request, id):
		book=self.get_object(id)
		serializer = BooksSerializer(book, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, id):
		book=self.get_object(id)
		book.delete()
		return Response(status=status.HTTP_204_No_CONTENT)