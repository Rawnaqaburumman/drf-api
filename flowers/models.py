from django.db import models
from django.contrib.auth import get_user_model



class Flowers(models.Model):
   name=models.CharField(max_length=64)
   description=models.TextField()
   user= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


   created_at = models.DateTimeField(auto_now_add = True ,auto_now = False )
   updated_at = models.DateTimeField(auto_now = True , auto_now_add = False)
   post = models.BooleanField(default=False)
   def __str__(self):
        return self.name




 
