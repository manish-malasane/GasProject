# Gas Utility Customer Service Application
The Gas Utility Customer Service Application is a Django-based web application designed to streamline the customer 
service experience for a gas utility company. The application allows customers to submit service requests online, track 
the status of their requests, and provides customer support representatives with tools to manage and support customer 
requests.

## Features
##### Service Requests:-
Customers can submit service requests online, including specifying the type of request, providing 
details, and attaching files if necessary.

##### Request Tracking:-
Customers can track the status of their service requests, including submission date, status updates,
and resolution details.

## Prerequisites
- Python 3.10
- Django (Install using pip install Django)

# Installation and Setup
#### Clone the repository:
- git clone https://github.com/manish-malasane/GasUtility.git
- cd GasUtilityP
- Create a virtual environment (optional but recommended):
- python3 -m venv venv
- On Linux :- source venv/bin/activate  (To activate virtual environment)
- On Windows:- venv\Scripts\activate    (To activate virtual environment)

### Install the project dependencies:
- pip install -r requirements.txt

##### Apply migrations:
- python manage.py makemigrations
- python manage.py migrate

##### Create a superuser:
- python manage.py createsuperuser

##### Start the development server:
- python manage.py runserver
- Access the application in your browser at http://127.0.0.1:8000/

## Usage
1. Navigate to the "Submit Service Request" page to submit a new service request.
2. Fill in the requested details, including request type, details, and optionally attach files.
3. Click "Submit" to create a new service request.
4. To track the status of service requests, navigate to the "Track Service Requests" page.
5. View a list of submitted requests, including their status, submission date, and resolution details.