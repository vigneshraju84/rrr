from django.db import models
from fbv.models import Author

class Books(models.Model):
	author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
	name= models.CharField(max_length=200)
	status= models.SmallIntegerField()
	created_on= models.DateTimeField(auto_now_add=True)
	modified_on= models.DateTimeField()
	
	def __str__(self):
		return self.name
		
	class Meta:
		db_table = "tbl_books"
		ordering = ["name"]
	