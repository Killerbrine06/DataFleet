# DataFleet
Backend Data Management System for Structured Operational Datasets

## Overview

DataFleet is a backend system designed to securely store, process, and analyze structured operational data in the shipyard domain.

The project focuses on backend architecture, relational database design, and scalable data processing workflows. It provides a modular Django-based structure that enables efficient data manipulation, statistical analysis, and future system expansion.

This project demonstrates backend engineering practices, database schema design, and structured API development using Python and Django.

---

## Tech Stack

- Python  
- Django  
- MySQL  
- GNU/Linux (development environment)

---

## Core Features

- Relational database schema optimized for structured datasets
- Secure CRUD operations for data manipulation
- RESTful backend architecture
- Data validation and integrity enforcement
- Modular Django app structure for maintainability
- Statistical data processing modules
- Designed for scalability and future feature expansion

---

## Architecture Overview

DataFleet follows a layered backend structure:

- **Models Layer** → Relational schema definition and data relationships  
- **API / View Layer** → Request handling and data processing  
- **Database Layer** → MySQL relational storage  
- **Business Logic Layer** → Statistical and operational processing  

The architecture is structured to allow future implementation of:

- Authentication and authorization systems
- Role-based access control
- Reporting modules
- Extended analytics features

---

## Installation & Setup

### 1. Clone the repository

    git clone https://github.com/Killerbrine06/DataFleet.git
    cd DataFleet

### 2. Create a virtual environment

    python -m venv venv

Activate the environment:

**Linux / macOS**

    source venv/bin/activate

**Windows**

    venv\Scripts\activate

### 3. Install dependencies

    pip install -r dependencies.txt

### 4. Configure environment variables

Set up your database credentials and required environment variables before running the project.

### 5. Apply migrations

    python manage.py migrate

### 6. Run the development server

    python manage.py runserver

The application will start locally and can be accessed via your browser.

---

## Example Use Cases

- Structured operational data storage  
- Statistical data querying and processing  
- Backend foundation for domain-specific management systems  
- Scalable data handling for analytics workflows  

---

## Project Status

This project is currently under active development.

Core backend architecture and database schema are implemented. Additional features and optimizations are planned to further expand analytical and system capabilities.

---

## Author

**Vlad George Cacenschi**  
Python Backend & Automation Developer  

---

## License

This project is intended for educational and portfolio purposes.
