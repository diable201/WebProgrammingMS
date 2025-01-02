# 🌟 Web Programming Fall 2024, M.Sc

Welcome to the repository for web programming e-learning platform project and assignments! This project is designed to enhance your skills in **Django**, **Docker**, and **Django Rest Framework (DRF)** through hands-on learning. Dive into containerization, web application development, and API creation while building a functional e-learning platform.

---

## 📜 Table of Contents

- [🌟 Web Programming Fall 2024, M.Sc](#-web-programming-fall-2024-msc)
  - [📜 Table of Contents](#-table-of-contents)
  - [🛠️ About](#️-about)
  - [✨ Features](#-features)
  - [📚 Assignments](#-assignments)
    - [Assignment 1: Introduction to Docker](#assignment-1-introduction-to-docker)
      - [📝 Objective](#-objective)
      - [🚀 Key Features](#-key-features)
    - [Assignment 2: Exploring Django with Docker](#assignment-2-exploring-django-with-docker)
      - [📝 Objective](#-objective-1)
      - [🚀 Key Features](#-key-features-1)
    - [Assignment 3: Advanced Django Development](#assignment-3-advanced-django-development)
      - [📝 Objective](#-objective-2)
      - [🚀 Key Features](#-key-features-2)
    - [Assignment 4: Building a RESTful API with DRF](#assignment-4-building-a-restful-api-with-drf)
      - [📝 Objective](#-objective-3)
      - [🚀 Key Features](#-key-features-3)
  - [🎓 Final Project: E-Learning Platform](#-final-project-e-learning-platform)
    - [🌟 Overview](#-overview)
      - [💻 Features](#-features-1)
      - [🛠️ Deliverables](#️-deliverables)
  - [💾 Requirements](#-requirements)
  - [📦 Installation and Setup](#-installation-and-setup)
    - [🛠️ Prerequisites](#️-prerequisites)
    - [📥 Steps](#-steps)
  - [⚙️ Usage](#️-usage)
  - [🤝 Contributing](#-contributing)
  - [📜 License](#-license)
  - [🙌 Acknowledgments](#-acknowledgments)

---

## 🛠️ About

This repository contains a series of assignments and a final project designed to:

- Teach the basics of **containerization** using Docker.
- Develop web applications using **Django** and **DRF**.
- Implement advanced features like API versioning, authentication, and deployment.
- Build a complete, containerized e-learning platform as a capstone project.

---

## ✨ Features

- 📦 **Containerization**: Efficient and portable deployment using Docker.
- 📄 **Dynamic Models**: Advanced relationships and queries in Django.
- 🌐 **RESTful APIs**: Robust API implementation with authentication and versioning.
- 🎨 **Frontend Integration**: Seamless interaction with a frontend framework.
- 🚀 **Scalable Deployment**: Ready for deployment on cloud platforms.

---

## 📚 Assignments

### Assignment 1: Introduction to Docker

#### 📝 Objective
Learn the basics of Docker, including installation, commands, and Dockerfile creation.

#### 🚀 Key Features
- Install Docker and verify with `docker run hello-world`.
- Use basic commands (`docker pull`, `docker run`, `docker ps`, etc.).
- Write and optimize a Dockerfile for a Python application.
- Push Docker images to Docker Hub.

---

### Assignment 2: Exploring Django with Docker

#### 📝 Objective
Set up a Django application with Docker Compose and learn about Docker networking and volumes.

#### 🚀 Key Features
- Configure services for Django and PostgreSQL in `docker-compose.yml`.
- Persist data using Docker volumes.
- Create a simple Django app and connect it to the database.

---

### Assignment 3: Advanced Django Development

#### 📝 Objective
Build a robust Django application focusing on models, views, and templates.

#### 🚀 Key Features
- Define models with relationships (e.g., `Post`, `Category`, `Comment`).
- Implement function-based and class-based views.
- Create dynamic templates with inheritance and static file integration.

---

### Assignment 4: Building a RESTful API with DRF

#### 📝 Objective
Develop a RESTful API using DRF with advanced features and deploy it using Docker.

#### 🚀 Key Features
- Create serializers and API views for CRUD operations.
- Add token-based authentication and custom permissions.
- Implement nested serializers, API versioning, and rate limiting.

---

## 🎓 Final Project: E-Learning Platform

### 🌟 Overview
The final project involves building a containerized e-learning platform using Django, Docker, and DRF. The platform will include:

#### 💻 Features
- **User Management**: Students and instructors with role-specific functionalities.
- **Course Management**: CRUD operations for courses, lessons, and quizzes.
- **RESTful API**: Full CRUD API for integration with a frontend framework.
- **Containerization**: Dockerized application for deployment.
- **Progress Tracking**: Track user progress, including completed lessons and quiz scores.

#### 🛠️ Deliverables
- Fully functional backend with DRF APIs.
- Frontend integration with dynamic views.
- Dockerized application ready for deployment.

---

## 💾 Requirements

- **Python**: Version 3.8+
- **Django**: Version 4.x
- **Docker**: Latest version
- **PostgreSQL**: Version 12+
- **Django Rest Framework (DRF)**: Latest version
- **Frontend Framework (Optional)**: React or Vue

---

## 📦 Installation and Setup

### 🛠️ Prerequisites
Ensure the following are installed:
- Docker and Docker Compose
- Python 3.x
- Postman or a similar API testing tool

### 📥 Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/diable201/WebProgrammingMS.git
   cd WebProgrammingMS
   ```
2. Build and run the application:
   ```bash
   docker-compose up --build
   ```
3. Access the application at `http://localhost:8000`.

---

## ⚙️ Usage

- **Run Tests**: 
  ```bash
  python manage.py test
  ```
- **Access API Endpoints**:
  Use Postman or Swagger UI to test RESTful APIs.
- **Modify Models**: Update `models.py` and run migrations:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review. Ensure your code follows best practices and includes documentation.

---

## 📜 License

This project is licensed under the `MIT` License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- **Django Documentation**: [Django Project](https://docs.djangoproject.com/)
- **Docker Documentation**: [Docker](https://docs.docker.com/)
- **DRF Documentation**: [Django Rest Framework](https://www.django-rest-framework.org/)
- **Inspiration**: Thanks to all contributors and the open-source community!

