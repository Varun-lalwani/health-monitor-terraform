# API Health Monitoring System

## Overview

This project is a **self-hosted API Health Monitoring System** built as part of the **DevOps Internship Assignment 2026**.

The system periodically checks the health of user-defined API endpoints, detects meaningful state changes (healthy ↔ unhealthy), and sends notifications when such changes occur. The solution is designed with **scalability, reliability, and operational clarity** in mind, without relying on any third‑party or managed monitoring services.

The focus of this project is **backend design, infrastructure automation, and DevOps thinking**, rather than UI or dashboards.

---

## Problem Statement

Organizations often depend on multiple internal and external APIs. Detecting downtime or degraded performance early is critical.

This system:

* Monitors configured API endpoints at regular intervals
* Evaluates health using user-defined criteria
* Tracks state transitions to avoid alert noise
* Sends notifications only when health state changes
* Runs fully on self-managed infrastructure

---

## Key Features

* Periodic API health checks
* Configurable endpoints and check intervals
* State-based alerting (no repeated alerts for same state)
* Lightweight and cost-efficient design
* Fully automated AWS infrastructure using Terraform
* Designed to scale horizontally

---

## System Architecture (High Level)

### Architecture Diagram

```
+-------------------+
|   Scheduler       |
| (Cron / Loop)     |
+---------+---------+
          |
          v
+-------------------+
| Health Checker    |
| (HTTP Probes)     |
+---------+---------+
          |
          v
+-------------------+
| State Evaluator   |
| (Compare States)  |
+----+----------+---+
     |          |
     |          v
     |   +------------------+
     |   | Notification     |
     |   | Service          |
     |   +------------------+
     |
     v
+-------------------+
| PostgreSQL (RDS)  |
| - Endpoints       |
| - Last State      |
+-------------------+
```

**Components:**

* **Health Checker Service**: Periodically sends HTTP requests to configured APIs
* **State Evaluator**: Compares current result with previous state
* **Persistence Layer**: Stores endpoint configs and last known state
* **Notification Module**: Sends alerts on state change
* **Scheduler**: Triggers health checks at defined intervals

**Flow:**

1. Scheduler triggers health check
2. Health checker probes API endpoint
3. Response is evaluated against rules
4. State is compared with previous result
5. Notification is sent only if state changed
6. State is persisted for next evaluation

---

## AWS Deployment Layout

### AWS Infrastructure Diagram

```
+-----------------------------+
|           AWS VPC           |
|                             |
|  +----------------------+   |
|  |      EC2 Instance    |   |
|  |  Health Monitor App  |   |
|  +----------+-----------+   |
|             |               |
|      Security Group          |
|             |               |
|  +----------v-----------+   |
|  |     RDS PostgreSQL    |   |
|  |  (Private Access)    |   |
|  +----------------------+   |
|                             |
+-----------------------------+
```

* EC2 hosts the monitoring service
* RDS stores configuration and health state
* Security Groups restrict network access
* IAM Role attached to EC2 follows least privilege

---

## Health Evaluation Logic

An endpoint is considered **healthy** when:

* HTTP response is successful (2xx)
* Response time is within acceptable limits

An endpoint is considered **unhealthy** when:

* HTTP request fails
* Non-2xx status code is returned
* Timeout occurs

Alerts are generated **only when the health state changes**, preventing alert fatigue.

---

## Scalability Design

The system is designed to scale by:

* Running health checks as stateless services
* Allowing horizontal scaling of compute instances
* Supporting batching and parallel health checks
* Decoupling monitoring logic from notification logic

In a production environment, this design can scale to monitor **thousands of APIs** by increasing compute capacity and distributing workloads.

---

## Infrastructure Design (AWS)

Infrastructure is provisioned using **Terraform** and includes:

* **EC2**: Hosts the health monitoring service
* **RDS (PostgreSQL)**: Stores endpoint configurations and health states
* **VPC & Security Groups**: Isolated networking and controlled access
* **IAM Roles**: Least-privilege access for EC2 to required AWS services

The system intentionally avoids managed monitoring services to comply with assignment constraints.

---

## Deployment Instructions

### Prerequisites

* AWS account
* Terraform installed
* AWS credentials configured

### Steps

```bash
terraform init
terraform validate
terraform apply
```

After deployment:

* EC2 instance runs the monitoring service
* RDS stores persistent health state
* Security groups allow controlled connectivity

---

## Security Considerations

* Least-privilege IAM roles
* Database not publicly accessible
* Security groups restrict inbound/outbound traffic
* Credentials managed via environment variables

---

## Design Decisions & Trade-offs

### Why a Single-Service Design?

* Faster implementation
* Easier debugging and operations
* Reduced deployment complexity

### Trade-offs

* Not event-driven in current version
* No UI/dashboard (intentionally excluded)
* Single-region deployment

These decisions were made to **prioritize reliability, clarity, and delivery speed**, with a clear upgrade path for future improvements.

---

## Future Improvements

* Multi-region deployment
* Event-driven architecture
* Retry/backoff strategies
* Alert aggregation and throttling
* Metrics and observability integration

---

## Assignment Alignment

This project fulfills all core expectations:

* ✔ API monitoring
* ✔ Health evaluation
* ✔ State change detection
* ✔ Notification logic
* ✔ Infrastructure-as-code
* ✔ Scalability and reliability reasoning

The focus is on **engineering judgment and system design**, as required by the assignment.

---

## Author

**Varun Lalwani**
DevOps Internship Assignment – 2026
