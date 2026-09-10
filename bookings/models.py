from django.db import models

# Create your models here.
from accounts.models import MyUser
from events.models import Event


class Booking(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    seats=models.IntegerField()
    amount=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,default="pending")
    order_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.event.name