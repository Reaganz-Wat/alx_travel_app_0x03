from rest_framework.routers import DefaultRouter
from .views import ListingViewsets, BookingViewsets, PaymentViewSet

router = DefaultRouter()
router.register(r'listings', ListingViewsets, basename='listing')
router.register(r'bookings', BookingViewsets, basename='booking')
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = router.urls