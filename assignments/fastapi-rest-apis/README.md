# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI and Pydantic so students learn how to define endpoints, validate request data, and return JSON responses.

## 📝 Tasks

### 🛠️ API Endpoints

#### Description
Create a FastAPI application with endpoints for managing a simple task list. The API should support retrieving all tasks, retrieving a single task by ID, and creating new tasks.

#### Requirements
Completed program should:

- Define at least three endpoints: `GET /tasks`, `GET /tasks/{id}`, and `POST /tasks`.
- Accept and return JSON payloads.
- Use path parameters to retrieve a task by its ID.
- Return appropriate HTTP status codes for success and error cases.

### 🛠️ Data Validation and Documentation

#### Description
Add Pydantic models for request and response validation, and verify that FastAPI generates interactive API docs.

#### Requirements
Completed program should:

- Define Pydantic models for task input and output data.
- Validate required fields and types for incoming requests.
- Provide clear validation errors when input is invalid.
- Expose automatic API documentation via `/docs` or `/redoc`.

## Example

Example request/response flow:

```
POST /tasks
{
  "title": "Write FastAPI assignment",
  "description": "Create endpoints and validate input"
}

200 OK
{
  "id": 1,
  "title": "Write FastAPI assignment",
  "description": "Create endpoints and validate input",
  "completed": false
}
```
