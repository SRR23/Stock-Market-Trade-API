
# Stock-Market-Trade API

This is a RESTful API for a trade platform built with Django and Django Rest Framework (DRF). The API allows users to create, read, update, and delete trade data.


## Features

- CRUD operations for trade data
- See all trade data with pagination
- Filter data by trade_code

## Installation

Follow these steps to set up and run the project locally:

    1. Clone the Repository

    First, clone the repository from GitHub:

    git clone https://github.com/SRR23/Stock-Market-Trade-API.git
    cd config

    2. Set Up a Virtual Environment
    Create and activate a virtual environment:

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # On Windows
    python -m venv venv
    venv\Scripts\activate

    3. Install Dependencies
    Install the required packages:

    pip install -r requirements.txt

    4. Apply Migrations
    Run database migrations:

    python manage.py migrate

    5. Create a Superuser (Optional)
    To access the Django admin panel, create a superuser:

    python manage.py createsuperuser
    Follow the prompts to set up your admin account.

    6. Run the Development Server
    Start the Django development server:

    python manage.py runserver

    The API will be available at:
    📌 http://127.0.0.1:8000/
    
## API Endpoints

    CRUD Operation:
        POST /api/trades/ # Create a Trade
        GET /api/trades/ # Show all Trade data
        PUT /api/trades/{id}/ # Update all fields
        PATCH /api/trades/{id}/ # Update few fields
        DELETE /api/trades/{id}/ # Delete One of trade data
    
    List and Filter Trade Data by Trade Code:
        GET /api/trades/trade-code/ # Show Trade Code List
        GET /api/trades/?trade-code=code # Filter by Trade Code
    
    Show Static JSON Data From JSON File:
        GET /api/json-data/ # List All JSON Data
        GET /api/json/trade-code/ # Show Trade Code List
        GET /api/json-data/?trade-code=code # Filter by Trade Code

## Technologies Used

    Python
    Django
    Django Rest Framework (DRF)
    SQLite
