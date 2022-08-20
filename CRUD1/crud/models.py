from django.db import models



class News(models.Model):
	title=models.CharField(max_length=150)
	content=models.TextField(blank=True)
	create_at=models.DateTimeField(auto_now_add=True)
	upload_at=models.DateTimeField(auto_now=True)
	photo=models.ImageField(upload_to='img/%Y/%m/%d/')
	is_published=models.BooleanField(default=True)







#CRUD1 terminlada ishlash 
# python manage.py shell
 # from crud.models import News
 # News(title='Yangilik1',content='Kontent News 1')
 # news1=_
 # news1.title
 # news1.content
 # news1.save()
 # from django.db import connection
  # connection.queries
  # news2=News(title='Yangilik2',content='Kontent Yangilik 2')
  # news4=News.objects.create(title='News 4', content='Kontent News 4')