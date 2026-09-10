from django.db import models
from accounts.models import MyUser
# Create your models here.
class Event(models.Model):
    organizer=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()
    venue=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    price=models.IntegerField()
    total_seats=models.IntegerField()
    available_seats=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name