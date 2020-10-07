from django.db import models

# Create your models here.
class User1(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='username')
    password = models.CharField(max_length=64,
                                verbose_name='password')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='time')
    
    class Meta:
        db_table = 'basic_user1'