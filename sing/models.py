from django.db import models

class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField() 
    debut = models.DateField()   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=100) 
    content = models.TextField()             
    release = models.DateField()             
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

