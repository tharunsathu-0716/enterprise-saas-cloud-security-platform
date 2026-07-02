# Enterprise SaaS Cloud Security & DevSecOps Platform

A cloud-native multi-tenant SaaS security platform designed to demonstrate modern Cloud Security, DevSecOps, and Infrastructure as Code (IaC) practices.

---

## Project Overview

This platform simulates an enterprise-grade security management solution capable of:

- User Authentication
- Role-Based Access Control (RBAC)
- Multi-Tenant SaaS Architecture
- Security Event Logging
- Cloud Security Monitoring
- Infrastructure Automation
- DevSecOps Workflows

Built using:

- FastAPI
- Python
- SQLAlchemy
- SQLite (Development)
- PostgreSQL (Planned)
- Docker
- Kubernetes
- Terraform
- AWS

---

## Current Project Status

### Phase 1 – Core SaaS Platform

#### Authentication

- [x] User Registration
- [x] User Login
- [x] Password Hashing (bcrypt)
- [x] JWT Token Generation
- [x] JWT Validation Logic
- [x] Protected Route Framework

#### Database

- [x] SQLAlchemy Integration
- [x] User Model
- [x] Database Session Management
- [x] SQLite Development Database

#### API

- [x] FastAPI Application Setup
- [x] Swagger Documentation
- [x] Authentication Router

#### Security

- [x] Password Security with bcrypt
- [x] Environment Variable Configuration
- [x] OAuth2/JWT Foundation

---

## Implemented Endpoints

### Authentication

#### Register User

```http
POST /auth/register
```
