from django.db import models

class Author(models.Model):
	name= models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	status = models.SmallIntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name
	class Meta:
		db_table = "tbl_author"
		ordering = ['name']
		