# Box Selection System

A Django REST API that recommends a suitable shipping box for a set of products based on product dimensions, quantity, weight, box dimensions, maximum weight capacity, and box cost.

The system supports multiple products, product quantities, product rotation, weight constraints, and selects the lowest-cost box that can accommodate all requested products.

---

## Features

- Product management using Django models
- Shipping box management using Django models
- REST API for box recommendations
- Support for multiple products in a single request
- Support for product quantities
- Product rotation/orientation support
- Total product weight validation
- Box maximum weight validation
- 3D product-to-box fitting logic
- Selection of the lowest-cost suitable box
- Validation for invalid product IDs and quantities
- Proper HTTP status codes for API responses
- Django Admin interface for managing products and boxes
- Automated test suite
- GitHub Actions for automated test execution

---

## Tech Stack

- Python 3.13
- Django
- Django REST Framework
- SQLite
- Django ORM
- GitHub Actions

---

## Project Structure

```text
box-selection-system/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── packaging/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── .gitignore
├── AI_USAGE.md
├── README.md
├── TEST_OUTPUT.md
├── manage.py
└── requirements.txt

---

## Setup Instructions

Follow these steps to set up and run the project locally.

### Prerequisites

Make sure you have the following installed:

- Python 3.13
- pip
- Git

Check your Python version:

```bash
python3 --version

1. Clone the Repository
git clone <YOUR_GITHUB_REPOSITORY_URL>

2. Create a Virtual Environment
python3 -m venv .venv

3. Activate the Virtual Environment
source .venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Run Database Migrations
python manage.py migrate

6. Create a Django Admin User
python manage.py createsuperuser
http://127.0.0.1:8000/admin

7. Start the Development Server
python manage.py runserver
http://127.0.0.1:8000/



Running the API

POST http://127.0.0.1:8000/api/recommend-box/

curl -X POST http://127.0.0.1:8000/api/recommend-box/ \
-H "Content-Type: application/json" \
-d '{
    "products": [
        {
            "product_id": 1,
            "quantity": 1
        },
        {
            "product_id": 2,
            "quantity": 1
        }
    ]
}'

Example Response
{
    "recommended_box": {
        "id": 2,
        "name": "Medium Box",
        "length": 50.0,
        "width": 35.0,
        "height": 20.0,
        "max_weight": 10.0,
        "cost": 80.0
    }
}

Running Tests:-
python manage.py test

The test suite covers:

Single product recommendation
Multiple product recommendation
Product quantity handling
Product rotation
Box weight limit
No suitable box
Invalid product ID
Invalid quantity
Empty product list
Missing products field

Detailed test output is also available in:TEST_OUTPUT.md
