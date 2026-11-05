# Secure Login System – DevOps Implementation

## Project Overview

Originally developed as a university project for CS471 Computer Security, this project was extended to apply practical DevOps skills.

## Key DevOps Practices

- Docker & Docker Compose: Containerization and application management.
- Git & GitHub: Version control and source code management.
- GitHub Actions: Automated CI workflows.
- Automated Testing: Unit testing using Python unittest.
- Docker Build: Automated image building through CI.

This project demonstrates practical application of DevOps tools to improve automation, testing, and development workflows.

## Technologies Used

- Python & Flask
- SQLite
- Docker & Docker Compose
- Gunicorn
- Git & GitHub
- GitHub Actions
- Python Unittest

## Running the Project

### Prerequisites
- Docker Desktop
- Docker Compose

### Build and Run


Clone the repository:

```bash
git clone https://github.com/Reemaaldajani/secure-login-system.git
```

Navigate to the project directory:

```bash
cd secure-login-system
```

Build and start the application:

```bash
docker compose up --build
```

Open the application in your browser:

http://localhost:5001

### Stop the Application

```bash
docker compose down
```


## Automated Testing

The project includes automated tests using Python unittest.

To run the tests locally:

```bash
python -m unittest discover -v
```
The tests are also executed automatically through GitHub Actions as part of the CI workflow.

## Continuous Integration (CI)

GitHub Actions automates the CI workflow whenever code is pushed or a pull request is created on the main branch.

The workflow includes:
- Checking out the repository.
- Setting up Python.
- Installing dependencies.
- Running automated tests.
- Building the Docker image.