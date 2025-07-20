# ALX Travel App 0x00

## Project Overview

This Django-based travel application provides a platform for managing property listings, bookings, and reviews. The project implements database modeling, API serialization, and data seeding functionality as part of the ALX Backend Development curriculum.

## Features

- **Property Listings Management**: Create and manage travel property listings
- **Booking System**: Handle guest bookings for properties
- **Review System**: Allow guests to leave reviews and ratings
- **API Serialization**: REST API endpoints with proper data serialization
- **Database Seeding**: Automated sample data population

## Project Structure

```
alx_travel_app/
├── alx_travel_app/
│   ├── listings/
│   │   ├── models.py              # Database models
│   │   ├── serializers.py         # API serializers
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed.py        # Database seeding command
│   │   └── ...
│   ├── manage.py
│   └── ...
└── README.md
```

## Database Models

### Listing Model
- **title**: Property title (CharField, max_length=200)
- **description**: Property description (TextField)
- **price**: Property price (DecimalField)
- **price_per_night**: Nightly rate (DecimalField)
- **location**: Property location (CharField, max_length=100)
- **available**: Availability status (BooleanField, default=True)
- **created_at**: Creation timestamp (DateTimeField, auto_now_add=True)
- **updated_at**: Update timestamp (DateTimeField, auto_now=True)

### Booking Model
- **listing**: Foreign key to Listing (CASCADE delete)
- **guest_name**: Guest name (CharField, max_length=255)
- **check_in**: Check-in date (DateField)
- **check_out**: Check-out date (DateField)
- **created_at**: Creation timestamp (DateTimeField, auto_now_add=True)

### Review Model
- **listing**: Foreign key to Listing (CASCADE delete)
- **reviewer_name**: Reviewer name (CharField, max_length=255)
- **rating**: Rating score (IntegerField)
- **comment**: Review comment (TextField, blank=True)
- **created_at**: Creation timestamp (DateTimeField, auto_now_add=True)

## API Serializers

The project includes serializers for:
- **ListingSerializer**: Handles Listing model serialization
- **BookingSerializer**: Handles Booking model serialization

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd alx_travel_app
   ```

2. **Set up virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django psycopg2-binary
   ```

4. **Configure database settings in settings.py**

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Database Seeding

The project includes a custom management command to populate the database with sample data.

### Running the Seed Command

```bash
python manage.py seed
```

### Sample Data Created

The seeding command creates:
- **5 Property Listings:**
  - Beach House (Malibu) - $250/night
  - Mountain Cabin (Alps) - $180/night
  - City Apartment (New York) - $300/night
  - Desert Villa (Nevada) - $150/night
  - Lake Cottage (Michigan) - $220/night

- **5 Sample Bookings** with different guests and date ranges
- **5 Sample Reviews** with ratings and comments

### Seeding Success Proof

The database seeding was successfully completed as shown in the terminal output:

![Database Seeding Success](/asset/seeding.png)

*Screenshot showing successful database seeding with all 5 listings, 5 bookings, and 5 reviews created.*

## Key Implementation Details

### Model Relationships
- **One-to-Many**: Listing → Bookings (one listing can have multiple bookings)
- **One-to-Many**: Listing → Reviews (one listing can have multiple reviews)

### Data Validation
- All models include appropriate field constraints and validation
- Foreign key relationships ensure data integrity
- DateTime fields automatically track creation and modification times

### Management Command Structure
- Custom command located in `listings/management/commands/seed.py`
- Uses Django's `get_or_create()` method to prevent duplicate entries
- Provides clear console feedback during seeding process
- Handles both creation and existing record scenarios

## Usage

### Running the Development Server
```bash
python manage.py runserver
```

### Accessing the Admin Interface
1. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
2. Visit `http://localhost:8000/admin/` to manage data

## Technical Requirements Met

✅ **Database Modeling**: All three models (Listing, Booking, Review) implemented with proper fields and relationships

✅ **Data Seeding**: Custom management command successfully populates database with sample data

✅ **Serializers**: API serializers created for Listing and Booking models

✅ **Project Structure**: Organized file structure following Django best practices

✅ **Data Integrity**: Proper foreign key relationships and constraints implemented

## Testing

The seeding functionality has been tested and verified to work correctly. The screenshot above demonstrates successful execution of the seed command with:
- 5 listings created successfully
- 5 bookings created successfully  
- 5 reviews created successfully
- All database constraints satisfied
- No integrity errors

## Future Enhancements

- User authentication and authorization
- Advanced search and filtering capabilities
- Payment integration
- Image upload for listings
- Email notifications for bookings
- API rate limiting and pagination

## Repository Information

- **GitHub Repository**: `alx_travel_app`
- **Directory**: `alx_travel_app`
- **Key Files**: 
  - `listings/models.py`
  - `listings/serializers.py`
  - `listings/management/commands/seed.py`
  - `README.md`

## Author

Reagan - ALX Backend Development Program

## License

This project is part of the ALX Software Engineering curriculum.