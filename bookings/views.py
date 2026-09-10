from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from bookings.models import Booking
from bookings.serializers import BookingSerializer


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from bookings.models import Booking
from bookings.serializers import BookingSerializer
from bookings.permissions import IsCustomerOnly



# class BookingAPI(generics.CreateAPIView):
#
#     queryset=Booking.objects.all()
#     serializer_class=BookingSerializer
#     permission_classes = [IsCustomerOnly]
#     def perform_create(self,serializer):
#         event=serializer.validated_data['event']
#         seats=serializer.validated_data['seats']
#
#         amount=event.price*seats
#
#         u=self.request.user
#
#         serializer.save(user=u,amount=amount)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import razorpay


# class BookingAPIView(APIView):
#     permission_classes = [IsCustomerOnly,]
#
#     def post(self,request):
#
#         serializer=BookingSerializer(data=request.data)
#
#         if serializer.is_valid():
#             event = serializer.validated_data['event']
#             seats = serializer.validated_data['seats']
#             amount = event.price * seats
#             booking=serializer.save(amount=amount,user=request.user)
#             client=razorpay.Client( auth=('rzp_test_TZ7X8lFGtbnbC3','z01ol71FXbLGAjM0V27g98j4'))
#             print(client)
#             # order creation
#             response_payment=client.order.create(dict(amount=amount * 100,currency="INR"))
#             print(response_payment)
#
#             booking.order_id=response_payment['id']
#             booking.save()

#
#
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BookingAPIView(APIView):
    permission_classes=[IsCustomerOnly]

    def post(self,request):
        serializer=BookingSerializer(data=request.data)
        if serializer.is_valid():
            event=serializer.validated_data['event']
            seats=serializer.validated_data['seats']
            amount=event.price*seats
            u=self.request.user
            booking=serializer.save(amount=amount,user=u)
            client=razorpay.Client(auth=('rzp_test_TZ7X8lFGtbnbC3','t70KTAiASGYyYQ0AYHtbjiGa'))
            print(client)
            response_payment = client.order.create(dict(amount=amount * 100, currency="INR"))
            print(response_payment)

            booking.order_id = response_payment['id']
            booking.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)

class Verifypayment(APIView):
    permission_classes=[IsCustomerOnly]

    def post(self,request):
        booking_id=request.data['booking_id']
        payment_id=request.data['razorpay_payment_id']
        order_id=request.data['razorpay_order_id']
        signature=request.data['razorpay_signature']

        booking=Booking.objects.get(order_id=order_id,user=request.user)

        # Payment verification
        try:
            client=razorpay.Client(auth=('rzp_test_TZ7X8lFGtbnbC', 't70KTAiASGYyYQ0AYHtbjiGa'))

            client.utility.verify_payment_signature({
                "razorpay_order_id": order_id,
                "razorpay_payment_id": payment_id,
                "razorpay_signature": signature})

            booking.status = "completed"
            booking.save()
            booking.event.available_seats=booking.event.available_seats-booking.seats
            booking.event.save()

            return Response({"msg": "Payment successfully completed"},status=status.HTTP_200_OK)

        except:
            return Response(
                {"msg": "Payment verification failed"},status=status.HTTP_400_BAD_REQUEST)

