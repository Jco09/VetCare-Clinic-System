# VetCare: Clinic Appointment Management System

**VetCare** is a web-based application designed for local pet clinics to digitize their appointment scheduling and patient record management. This project replaces manual logbooks with a modern, decoupled system using a Django REST API and a responsive frontend.

## Tech Stack
* **Backend:** Django, Django REST Framework (DRF)
* **Frontend:** HTML5, JavaScript (Fetch API), Tailwind CSS
* **Database:** SQLite

## Features
* **Owner Management:** Register and manage pet owner contact details.
* **Pet Records:** Track patient names and species linked to specific owners.
* **Appointment Scheduling:** Book clinic visits with specific dates, times, and reasons.
* **Status Tracking:** Update appointments from "Scheduled" to "Completed."
* **RESTful API:** Fully documented API endpoints for all modules.

## Project Structure
```text
VetCare/
├── backend/            # Django Project & API
│   ├── api/            # Serializers, Views, and Models
│   ├── core/           # Project settings and URL routing
│   └── manage.py
├── frontend/           # UI Files
│   ├── index.html      # Appointments Dashboard
│   ├── owners.html     # Owner Registration
│   └── pets.html       # Pet Management
└── requirements.txt    # Python Dependencies
