# FastAPI Assessment Problem Statement -- Student Management API

## Overview

Build a FastAPI application that manages student information for a small
training institute.\
The API must support full **CRUD operations**.

------------------------------------------------------------------------

## Student Object Structure

  Field    Type    Description
  -------- ------- ----------------------------------------------
  id       int     Auto-increment or unique ID
  name     str     Student's full name
  age      int     Age of the student
  course   str     Course enrolled (e.g., Python, Data Science)
  score    float   Test score (0--100)

------------------------------------------------------------------------

## Requirements

### 1. Create a Student

-   **POST /students**
-   Accepts student data
-   Returns created student

### 2. Read All Students

-   **GET /students**
-   Returns all students

### 3. Read a Single Student

-   **GET /students/{student_id}**
-   Returns student by ID
-   Return 404 if not found

### 4. Update a Student

-   **PUT /students/{student_id}**
-   Updates all fields
-   Return 404 if not found

### 5. Delete a Student

-   **DELETE /students/{student_id}**
-   Deletes the student

------------------------------------------------------------------------

## Storage

You may use: - In-memory list/dictionary - Optional: SQLite DB

------------------------------------------------------------------------

## Extra Credit (Optional)

Add:

-   **GET /students/topper**\
    Returns student with highest score.

------------------------------------------------------------------------

Good luck!
