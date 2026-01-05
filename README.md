# Automated CI/CD Pipeline for a Two-Tier Flask Application on AWS

**Author:** Bhavya Reddy Ganta  
**Date:** January 2026  
**Repository:** https://github.com/gantab665/two-tier-flask-mysql-jenkins

---

## Table of Contents

1. Project Overview  
2. Architecture Overview  
3. AWS EC2 Instance Preparation  
4. Installing Dependencies on EC2  
5. Jenkins Installation and Setup  
6. GitHub Repository Configuration  
7. Jenkins Pipeline Creation and Execution  
8. Application Access  
9. Conclusion  

---

## 1. Project Overview

This project demonstrates an **end-to-end DevOps CI/CD pipeline** for deploying a **two-tier web application (Flask + MySQL)** on **AWS EC2**.

The application is containerized using **Docker** and orchestrated with **Docker Compose**.  
A **Jenkins CI/CD pipeline** automates the build and deployment process whenever changes are pushed to the GitHub repository.

### Key Objectives:
- Automate application deployment using Jenkins
- Containerize application using Docker
- Use Docker Compose for multi-container orchestration
- Deploy on AWS EC2 (t2.micro, us-east-1)
- Demonstrate real-world DevOps workflow

---

## 2. Architecture Overview

High-level workflow of the project:

- Developer pushes code to GitHub
- Jenkins pulls the latest code
- Jenkins builds Docker images
- Jenkins runs Docker Compose
- Flask application communicates with MySQL container
- Application is exposed via public EC2 IP

**Components Used:**
- AWS EC2 (Ubuntu 22.04 LTS)
- GitHub
- Jenkins
- Docker & Docker Compose
- Flask
- MySQL

---

## 3. AWS EC2 Instance Preparation

### EC2 Configuration:
- **AMI:** Ubuntu 22.04 LTS
- **Instance Type:** t2.micro
- **Region:** us-east-1
- **Key Pair:** Used for SSH access

### Security Group Inbound Rules:
- SSH — TCP 22 — Source: Your IP
- HTTP — TCP 80 — Source: Anywhere (0.0.0.0/0)
- Flask App — TCP 5000 — Source: Anywhere (0.0.0.0/0)
- Jenkins — TCP 8080 — Source: Anywhere (0.0.0.0/0)

---

## 4. Installing Dependencies on EC2

After connecting to the EC2 instance, the following tools are installed:

- Docker
- Docker Compose
- Git
- Java (required for Jenkins)

The system is updated and Docker is configured to run without sudo.

---

## 5. Jenkins Installation and Setup

- Jenkins is installed on the same EC2 instance
- Jenkins runs on port **8080**
- Initial admin password is retrieved from the server
- Required plugins are installed:
  - Pipeline
  - Git
  - Docker Pipeline

Jenkins is used to automate the CI/CD workflow.

---

## 6. GitHub Repository Configuration

The GitHub repository contains:

- `Dockerfile` — Builds Flask application image
- `docker-compose.yml` — Defines Flask and MySQL services
- `Jenkinsfile` — Defines CI/CD pipeline stages
- `app/` — Flask application source code

GitHub credentials are securely added to Jenkins using the **Credentials Manager**.

---

## 7. Jenkins Pipeline Creation and Execution

### Pipeline Workflow:
1. Clone GitHub repository
2. Build Docker images
3. Start containers using Docker Compose
4. Deploy the application

The pipeline is triggered manually or on code changes and completes without manual intervention.

---

## 8. Application Access

Once deployment is successful, services are accessible using the EC2 public IP:

- **Flask Application:**  http://<EC2_PUBLIC_IP>:5000
- **Jenkins Dashboard:**  http://<EC2_PUBLIC_IP>:8080


MySQL runs internally and is not exposed publicly.

---

## 9. Conclusion

This project successfully demonstrates how to build and deploy a **production-style CI/CD pipeline** using Jenkins, Docker, and AWS EC2.

It highlights core DevOps concepts such as:
- Continuous Integration and Deployment
- Infrastructure configuration
- Containerization
- Automation

This setup can be extended further using load balancers, auto-scaling, monitoring, and cloud-native CI/CD tools.

---



