from django.db import models

# id -INT
#title-Varchar
#content-Text
#crate_at-DateTime
#update_at-DateTime
#is_published -Boolean

class News(models.Model):
	title=models.CharField(max_length=150)
	content=models.TextField(blank=True)
	create_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now=True)
	photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
	is_published=models.BooleanField(default=True)








# python manage.py sqlmigrate news 0001

