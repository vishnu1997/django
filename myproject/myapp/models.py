from django.db import models

# Create your models here.
class myproject(models.Model):
    name = models.CharField(max_length=100)
    regno = models.DecimalField(max_digits=13, decimal_places=0)
    cgpa = models.DecimalField(max_digits=13, decimal_places=4)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    img_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name+"---"+str(self.regno)