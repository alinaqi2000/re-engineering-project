# Student Management REST API

Welcome to the Student Management REST API project! This API is designed to perform CRUD (Create, Read, Update, Delete) operations for storing basic information about students in a JSON file on the server. It's built using Flask, a lightweight and easy-to-use web framework for Python.

## Features

- Create a new student record with their details.
- Retrieve a list of all students or specific student details.
- Update the information of an existing student.
- Delete a student record from the system.
- Store student data in a JSON file for persistence.

## Installation Guide

To run this project locally, follow these steps:

### Prerequisites

- Python 3.\*
- [Virtualenv (for library management)](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)

### 1. Clone the Repository

First, clone this repository to your local machine using Git:

```bash
git clone https://github.com/alinaqi2000/scd-project.git
```

### 2. Create a Virtual Environment

Navigate to the project directory and create a virtual environment to isolate your project dependencies:

```bash
cd scd-project
virtualenv venv
```

Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```

On macOS and Linux:

```bash
source venv/bin/activate
```

### 3. Run the Application

Run the Flask application with the following command:

```bash
flask --debug run
```

By default, the API will be available at `http://localhost:5000/`.

### 4. Access the API

You can now access the API using a tool like [Postman](https://www.postman.com/) or by creating your own client application. Here are some example API endpoints:

- `GET /get-all-students`: Get a list of all students.
- `GET /get-student/<studentID>`: Get details of a specific student.
- `POST /save-student`: Create a new student.
- `PUT /update-student/<studentID>`: Update a student's information.
- `DELETE /delete-student/<studentID>`: Delete a student.

Remember to replace `<studentID>` with the actual ID of the student you want to interact with.

## Contribution

If you'd like to contribute to this project, please fork the repository, create a new branch for your changes, and submit a pull request. We welcome any enhancements or bug fixes!

Thank you for using the Student Management REST API. Happy coding!
