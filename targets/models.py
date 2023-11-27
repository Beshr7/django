from django.db import models


# Create your models here.
class Target_model(models.Model):
    label = models.CharField(max_length=200)
    target_id = models.CharField(max_length=200)
    # target_id = models.TextField()
    time_created = models.DateTimeField("date created")
    # time_current = models.TextField(default="0")
    new_field = models.IntegerField(default=0)
    new_field2 = models.CharField(max_length=200, default="default")

    def __str__(self):
        return self.label
