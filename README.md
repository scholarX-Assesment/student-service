# Student Service API

This API provides CRUD operations for managing students, academic histories, and courses.

## Endpoints

### Students

- **Create Student**
  - **URL:** `/students/`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "name": "string",
      "age": "integer",
      "email": "string"
    }
    ```
  - **Response:**
    ```json
    {
      "id": "integer",
      "name": "string",
      "age": "integer",
      "email": "string"
    }
    ```

- **Get Student**
  - **URL:** `/students/{student_id}`
  - **Method:** `GET`
  - **Response:**
    ```json
    {
      "id": "integer",
      "name": "string",
      "age": "integer",
      "email": "string"
    }
    ```

- **Get Students**
  - **URL:** `/students/`
  - **Method:** `GET`
  - **Query Parameters:**
    - `skip`: integer (default: 0)
    - `limit`: integer (default: 10)
  - **Response:**
    ```json
    [
      {
        "id": "integer",
        "name": "string",
        "age": "integer",
        "email": "string"
      }
    ]
    ```

- **Delete Student**
  - **URL:** `/students/{student_id}`
  - **Method:** `DELETE`
  - **Response:**
    ```json
    {
      "id": "integer",
      "name": "string",
      "age": "integer",
      "email": "string"
    }
    ```

### Academic History

- **Create Academic History**
  - **URL:** `/students/{student_id}/academic-history/`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "course_name": "string",
      "grade": "string"
    }
    ```
  - **Response:**
    ```json
    {
      "id": "integer",
      "course_name": "string",
      "grade": "string",
      "student_id": "integer"
    }
    ```

- **Get Academic History**
  - **URL:** `/students/{student_id}/academic-history/`
  - **Method:** `GET`
  - **Response:**
    ```json
    [
      {
        "id": "integer",
        "course_name": "string",
        "grade": "string",
        "student_id": "integer"
      }
    ]
    ```

### Courses

- **Create Course**
  - **URL:** `/courses/`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "name": "string",
      "description": "string"
    }
    ```
  - **Response:**
    ```json
    {
      "id": "integer",
      "name": "string",
      "description": "string"
    }
    ```

- **Get Course**
  - **URL:** `/courses/{course_id}`
  - **Method:** `GET`
  - **Response:**
    ```json
    {
      "id": "integer",
      "name": "string",
      "description": "string"
    }
    ```

- **Get Courses**
  - **URL:** `/courses/`
  - **Method:** `GET`
  - **Query Parameters:**
    - `skip`: integer (default: 0)
    - `limit`: integer (default: 10)
  - **Response:**
    ```json
    [
      {
        "id": "integer",
        "name": "string",
        "description": "string"
      }
    ]
    ```

### Enrollments

- **Enroll Student in Course**
  - **URL:** `/students/{student_id}/courses/{course_id}`
  - **Method:** `POST`
  - **Response:**
    ```json
    {
      "student_id": "integer",
      "course_id": "integer"
    }
    ```

- **Get Student Courses**
  - **URL:** `/students/{student_id}/courses/`
  - **Method:** `GET`
  - **Response:**
    ```json
    [
      {
        "id": "integer",
        "name": "string",
        "description": "string"
      }
    ]
    ```