# Student Service API

This API provides CRUD operations for managing students, academic histories, and courses.

## Service Information

The Student Service API is designed to manage student records, academic histories, and course enrollments. It provides endpoints to create, read, update, and delete student information, as well as manage academic histories and course enrollments.

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL
- SQLAlchemy
- FastAPI

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/student-service.git
    cd student-service
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    - Create a PostgreSQL database.
    - Update the database URL in the `database.py` file.

5. Run the migrations to set up the database schema:
    ```sh
    alembic upgrade head
    ```

6. Start the FastAPI server:
    ```sh
    uvicorn main:app --reload
    ```

7. Access the API documentation at `http://127.0.0.1:8000/docs`.
