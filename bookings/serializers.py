from rest_framework import serializers
from bookings.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'
        read_only_fields=['user','amount','created_at','status','order_id']