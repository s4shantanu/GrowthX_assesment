# Assignment Submission Portal

```bash
# Features
- Users: Register, login, upload assignments.
- Admins: Register, login, view, accept/reject assignments.

# Tech Stack
- Framework: Django
- Database: MongoDB
- API Testing: Postman

# Installation
git clone https://github.com/username/assignment-submission-portal.git
cd assignment-submission-portal
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure MongoDB in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'assignment_portal',
        'CLIENT': {
            'host': 'mongodb://localhost:27017',
        }
    }
}

# Run Server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# API Endpoints
# User Endpoints
POST /register         # User registration
POST /login            # User login
POST /upload           # Upload assignment

# Admin Endpoints
POST /register         # Admin registration
POST /login            # Admin login
GET  /assignments      # View assignments
POST /assignments/:id/accept  # Accept assignment
POST /assignments/:id/reject  # Reject assignment

# Folder Structure
assignment-submission-portal/
├── core/                  # App logic and models
├── assignment_submission_portal/ # Project settings
├── requirements.txt       # Dependencies
└── README.md              # Documentation
