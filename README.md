# Smart Wellness Tracker

## Overview

Smart Wellness Tracker is a full-stack wellness monitoring application designed to collect, manage, and analyze employee wellness data. The application enables users to record mood, stress levels, energy levels, and wellness notes while providing real-time analytics through an interactive dashboard.

The project was developed to strengthen skills in software development, database management, software testing, and quality assurance practices. It demonstrates end-to-end application development, data persistence, input validation, dashboard reporting, and automated testing.

---

## Features

### Wellness Data Management

* Record employee wellness information, including mood, stress level, energy level, and notes
* Store and retrieve wellness records using MySQL
* Display historical wellness data in an interactive tabular format

### Analytics Dashboard

* Total wellness entries
* Average stress level tracking
* Average energy level tracking
* Mood distribution visualization

### Data Validation

* Mandatory employee name validation
* Stress level validation (1–10 range)
* Energy level validation (1–10 range)

### Automated Testing

* Unit tests implemented using PyTest
* Validation logic tested through positive and negative test scenarios
* Automated verification of business rules and application functionality

---

## Technology Stack

| Category        | Technologies |
| --------------- | ------------ |
| Frontend        | Streamlit    |
| Backend         | Python       |
| Database        | MySQL        |
| Data Processing | Pandas       |
| Testing         | PyTest       |
| Version Control | Git, GitHub  |

---

## Project Architecture

User Interface (Streamlit)

↓

Python Application Logic

↓

MySQL Database

---

## Testing Approach

The project incorporates software quality assurance practices through automated testing.

### Test Coverage

* Employee name validation
* Stress level boundary validation
* Energy level boundary validation
* Positive and negative test scenarios

### Sample Test Cases

| Test Case          | Input       | Expected Result |
| ------------------ | ----------- | --------------- |
| Valid Name         | "Keerthana" | Pass            |
| Blank Name         | ""          | Fail            |
| Valid Stress       | 5           | Pass            |
| Stress Above Limit | 15          | Fail            |
| Stress Below Limit | 0           | Fail            |
| Valid Energy       | 8           | Pass            |
| Energy Above Limit | 20          | Fail            |

---

## Key Learning Outcomes

* Building full-stack applications using Python and MySQL
* Implementing data validation and business rules
* Developing interactive dashboards using Streamlit
* Writing automated tests using PyTest
* Applying software quality assurance principles
* Managing source code using Git and GitHub

---

## Future Enhancements

* REST API development using FastAPI
* API testing and automation
* User authentication and role-based access
* Advanced wellness analytics and reporting
* Continuous Integration (CI/CD) pipeline
* Test coverage reporting

---

## Author

Keerthana Tatikonda

M.S. Computer Science | Software Development | Data Analytics | Quality Assurance
