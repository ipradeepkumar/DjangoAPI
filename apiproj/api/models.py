from django.db import models
import uuid

# Create your models here.

class Task(models.Model):
    TaskID: models.IntegerField()
    GUID = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    Status = models.CharField(max_length=50, null=True, default="PENDING")
    TotalIterations = models.IntegerField()

