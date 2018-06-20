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
    
    class Meta:
        permissions = (
            ("view_task", "Can see available tasks"),
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        )

class groupreq(models.Model):
    name = models.CharField(max_length=100)
    groupReq = models.CharField(max_length=100)

    def __str__(self):
        return self.name+" requested for joining "+str(self.groupReq)

