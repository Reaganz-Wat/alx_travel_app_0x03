import requests
from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Listing, Booking, Payment
from .serializers import ListingSerializer, BookingSerializer, PaymentSerializer

# Create your views here.
class ListingViewsets(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    
class BookingViewsets(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @action(detail=False, methods=["post"])
    def initiate(self, request):
        booking_ref = request.data.get("booking_reference")
        amount = request.data.get("amount")
        email = request.data.get("email")

        if not all([booking_ref, amount, email]):
            return Response(
                {"error": "booking_reference, amount, and email are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        payload = {
            "amount": str(amount),
            "currency": "ETB",  # change if needed
            "email": email,
            "tx_ref": booking_ref,
            "callback_url": "http://localhost:8000/api/payments/verify/",
            "return_url": "http://localhost:8000/payment-success/",
            "customization[title]": "Travel Booking Payment",
            "customization[description]": f"Payment for booking {booking_ref}",
        }

        headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}

        response = requests.post(
            f"{settings.CHAPA_BASE_URL}/initialize", json=payload, headers=headers
        )

        if response.status_code == 200:
            data = response.json()
            checkout_url = data["data"]["checkout_url"]
            transaction_id = data["data"]["tx_ref"]

            Payment.objects.create(
                booking_reference=booking_ref,
                amount=amount,
                transaction_id=transaction_id,
                status="Pending",
            )

            return Response({"checkout_url": checkout_url, "transaction_id": transaction_id})
        else:
            return Response(
                {"error": "Failed to initiate payment"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(detail=False, methods=["get"])
    def verify(self, request):
        tx_ref = request.query_params.get("tx_ref")

        if not tx_ref:
            return Response(
                {"error": "Transaction reference (tx_ref) required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}
        response = requests.get(
            f"{settings.CHAPA_BASE_URL}/verify/{tx_ref}", headers=headers
        )

        if response.status_code == 200:
            data = response.json()
            status_msg = data["data"]["status"]

            try:
                payment = Payment.objects.get(transaction_id=tx_ref)
                if status_msg == "success":
                    payment.status = "Completed"
                else:
                    payment.status = "Failed"
                payment.save()
            except Payment.DoesNotExist:
                return Response(
                    {"error": "Payment not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            return Response({"status": payment.status})
        else:
            return Response(
                {"error": "Verification failed"},
                status=status.HTTP_400_BAD_REQUEST,
            )