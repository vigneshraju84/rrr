from rest_framework import serializers
from .models import Author

class AuthorSerializers(serializers.ModelSerializer):
	class Meta:
		model = Author
		
		# fields = ['id','name','email','status','created_on']
		fields = "__all__"
		