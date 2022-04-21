
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from User.models import User
from shop.models import Product

class Action(models.Model):
    class  Meta:
        constraints=[
            models.UniqueConstraint(fields=['user','object_id'],name='unique_action') 
        ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,related_name='action')
    object_id = models.CharField(max_length=20) 
    content_object = GenericForeignKey()
      
class Comment(models.Model):
    id=models.CharField(max_length=20,primary_key=True) 
    body = models.TextField(blank=True)
    
    def __str__(self):
        return self.body

