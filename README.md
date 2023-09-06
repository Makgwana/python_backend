# python_backend
# Django REST Framework API with User Authentication and PostgreSQL

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [User Authentication](#user-authentication)
- [Admin Dashboard](#admin-dashboard)
- [App Health Status](#app-health-status)
- [Running Unit Tests](#running-unit-tests)
- [License](#license)

## Introduction

This Django REST Framework-based API provides authentication features, user registration, user and admin dashboards, app health status monitoring, and unit tests. It's designed to be a foundation for building secure web applications with Django and PostgreSQL.

## Features

- User Registration and Authentication
- User Dashboard
- Admin Dashboard
- App Health Status Monitoring
- Unit Testing

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
2. Install dependencies: 
    pip install -r requirements.txt

3. Configure your PostgreSQL database in settings.py
    python manage.py migrate

4. Start the development server:
    python manage.py runserver

5. Access the API at http://localhost:8000/api/.

API Endpoints
/api/users/register/: User registration.
/api/auth/login/: User login and token retrieval.
/api/userdashboard/: User dashboard.
/api/admindashboard/: Admin dashboard.
/api/health-check/: App health status.

Admin Dashboard
The admin dashboard provides administrative control over the application. You can manage users, view logs, and perform other administrative tasks.

App Health Status
The /api/health/ endpoint provides information about the application's health status, such as server uptime, database connectivity, and more.

Running Unit Tests

python manage.py test api

