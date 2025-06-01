# Swim Class Enrollment CLI

## Overview

This is a command-line interface (CLI) application for managing swim class enrollments. It allows you to manage swimmers, instructors, and their enrollments efficiently using a SQLite database with SQLAlchemy ORM.

The application includes:

- Listing and adding swimmers
- Listing and adding instructors
- Viewing enrollments of swimmers with instructors
- Enrolling swimmers to instructors
- Resetting all data (clearing database tables while keeping table structure)

## Features

- CLI menu-driven interface for ease of use
- Data persistence using SQLAlchemy ORM with SQLite
- Input validation for age, levels, and certifications
- Proper database session management
- Clear confirmation before resetting all data

## Requirements

- Python 3.8+
- [Pipenv](https://pipenv.pypa.io/en/latest/) for environment and dependency management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kabogo-Maverick/swimmers.git
   cd swimmers
2.Install dependencies>>>

  pipenv install
  pipenv shell

3.Initialize the database>>>
  python lib/seed.py

4.Run the main CLI application>>>
  python run.py

you will see;
Swim Class Enrollment CLI
1. List Swimmers
2. Add Swimmer
3. List Instructors
4. Add Instructor
5. List Enrollments
6. Enroll Swimmer
7. Reset All Data
8. Quit
Choose an option:


NOTE:Option 7 allows you to delete all data from the tables without dropping the tables themselves.
This is irreversible, so confirmation is required.



