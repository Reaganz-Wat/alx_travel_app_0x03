from datetime import timedelta, date
from random import choice, randint
from django.core.management.base import BaseCommand

# Since the app is registered as 'listings', try direct import
try:
    from alx_travel_app_0x03.listings.models import Listing, Booking, Review
except ImportError:
    # Fallback to app registry method
    from django.apps import apps

    Listing = apps.get_model('listings', 'Listing')
    Booking = apps.get_model('listings', 'Booking')
    Review = apps.get_model('listings', 'Review')


class Command(BaseCommand):
    help = "Seed the database with sample listings, bookings, and reviews"

    def handle(self, *args, **kwargs):
        self.stdout.write("🌱 Starting database seeding...")

        listing_data = [
    {"title": "Beach House", "description": "Nice beachside stay", "location": "Malibu", "price_per_night": 250},
    {"title": "Mountain Cabin", "description": "Secluded and cozy", "location": "Alps", "price_per_night": 180},
    {"title": "City Apartment", "description": "Downtown with skyline view", "location": "New York", "price_per_night": 300},
    {"title": "Desert Villa", "description": "Peaceful desert retreat", "location": "Nevada", "price_per_night": 150},
    {"title": "Lake Cottage", "description": "Waterfront escape", "location": "Michigan", "price_per_night": 220},
]


        listings = []
        for data in listing_data:
            listing, created = Listing.objects.get_or_create(**data)
            listings.append(listing)
            if created:
                self.stdout.write(f"Created listing: {listing.title}")
            else:
                self.stdout.write(f"Listing already exists: {listing.title}")

        self.stdout.write("✅ Seeded 5 listings.")

        # --- Seed Bookings ---
        for i in range(5):
            listing = choice(listings)
            check_in = date.today() + timedelta(days=i * 3)
            check_out = check_in + timedelta(days=2)

            booking, created = Booking.objects.get_or_create(
                listing=listing,
                guest_name=f"Guest {i + 1}",
                check_in=check_in,
                check_out=check_out
            )
            if created:
                self.stdout.write(f"Created booking for: {booking.guest_name}")
            else:
                self.stdout.write(f"Booking already exists for: {booking.guest_name}")

        self.stdout.write("✅ Seeded 5 bookings.")

        # --- Seed Reviews ---
        for i in range(5):
            listing = choice(listings)
            review, created = Review.objects.get_or_create(
                listing=listing,
                reviewer_name=f"Reviewer {i + 1}",
                defaults={
                    'rating': randint(1, 5),
                    'comment': f"This is review {i + 1}"
                }
            )
            if created:
                self.stdout.write(f"Created review by: {review.reviewer_name}")
            else:
                self.stdout.write(f"Review already exists by: {review.reviewer_name}")

        self.stdout.write("✅ Seeded 5 reviews.")
        self.stdout.write(self.style.SUCCESS("🎉 Database seeded successfully!"))