from django.db import models

# Create your models here.

class newsItem(models.Model):
    newsManage=models.Manager()
    title=models.CharField(max_length=100)
    publicTime=models.DateTimeField()
    publicContent=models.TextField()
    visitCount=models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-publicTime']    #排序
        db_table='newsItem'
