# Smart Wellness Tracker

## Overview

Smart Wellness Tracker is a full-stack wellness monitoring application developed using Python, Streamlit, MySQL, FastAPI, and PyTest. The application enables users to record wellness information, monitor wellness trends, and analyze employee wellness metrics through an interactive dashboard.

The project was built to demonstrate software development, database integration, API development, software testing, and quality assurance practices.

---

## Features

### Wellness Tracking

* Record employee wellness information
* Track mood, stress level, and energy level
* Store wellness records in MySQL

### Analytics Dashboard

* Total wellness entries
* Average stress level
* Average energy level
* Mood distribution visualization

### API Development

* GET /entries endpoint to retrieve wellness records
* POST /add-entry endpoint to add wellness records
* Interactive API testing through Swagger UI

### Validation

* Employee name validation
* Stress level range validation
* Energy level range validation

### Automated Testing

* PyTest unit tests for validation logic
* API automation tests using FastAPI TestClient
* 9 automated test cases passing

---

## Technology Stack

| Layer           | Technology   |
| --------------- | ------------ |
| Frontend        | Streamlit    |
| Backend         | Python       |
| Database        | MySQL        |
| API Framework   | FastAPI      |
| Data Processing | Pandas       |
| Testing         | PyTest       |
| Version Control | Git & GitHub |

---

## Project Structure

smart-wellness-tracker/

├── app.py

├── api.py

├── validation.py

├── requirements.txt

├── README.md

└── tests/

    ├── test_validation.py

    └── test_api.py

---

## Test Coverage

### Validation Tests

* Valid employee name
* Blank employee name
* Valid stress level
* Invalid stress level (high)
* Invalid stress level (low)
* Valid energy level
* Invalid energy level

### API Tests

* Home endpoint validation
* Wellness entries endpoint validation

Total Automated Tests: **9 Passed**

---

## Learning Outcomes

* Full-stack application development
* MySQL database integration
* REST API development using FastAPI
* Automated testing with PyTest
* API testing and validation
* Software Quality Assurance practices
* Git and GitHub version control

---

## Future Enhancements

* Advanced API validation
* Negative API testing
* HTML test reports
* Authentication and authorization
* CI/CD pipeline integration
* Cloud deployment

---

## Author

Lakshmi Keerthana Tatikonda

M.S. Computer Science

Data Analytics | Quality Assurance
