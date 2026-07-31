# Bulk Notification API

A Django REST Framework API that allows a sender to create multiple notifications in a single API request.
The API supports bulk notification creation across different channels such as email, SMS, and push notifications.

## Technologies Used

- Python 3.13
- Django 6
- Django REST Framework
- SQLite

## Setup Instructions

### 1. Clone the repository

```bash
git clone <https://github.com/paulMuema/bulk_sms_api.git>
cd bulk_sms_api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

The API will be available locally at: 
http://127.0.0.1:8000/

## API Documentation

### Bulk Create Notifications

**Endpoint**

POST /api/notifications/bulk/

**Request Body**

Example:

```json
{
    "name": "Alice Kamau",
    "email": "alice@example.com",
    "notifications": [
        {
            "title": "Welcome",
            "message": "Thank you for joining us.",
            "channel": "email"
        },
        {
            "title": "Reminder",
            "message": "Your subscription renews tomorrow.",
            "channel": "sms"
        }
    ]
}
```

**Successful Response**

Status Code: 201 Created

Response:

```json
{
    "message": "Notifications created successfully.",
    "sender_id": 1,
    "notifications_created": 2
}
```

**Validation Errors**

The API validates all incoming data before saving anything to the database.

Example:

```json
{
    "email": [
        "Enter a valid email address."
    ]
}
```

Status Code: 400 Bad Request

## Running Tests

```bash
python manage.py test
```