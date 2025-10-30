# 🏥 Case Study Project: “Smart Hospital Workflow System”

### 🎯 Objective

To design a Smart Hospital Workflow System that automates and coordinates multiple aspects of hospital operations — from patient intake to treatment and billing — using Behavioral Design Patterns to achieve flexibility, modularity, and maintainability.

### 🧠 Realistic Scenario

A hospital receives patients with various medical conditions.
Depending on the type and severity of the issue, requests move through different departments (triage, doctor, pharmacy, billing).
The system should also allow:

    - Undoing/redoing certain actions (e.g., reverting medication changes)
    - Notifications when important changes occur (like patient discharge)
    - Coordination among multiple components without tight coupling
    - Visiting different entities (patients, bills, records) for analytics

### 🧩 Design Patterns Applied

Pattern	Applied To	Purpose

| Pattern                     | Applied To              | Purpose                                                                                                                 |
| --------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Chain of Responsibility** | Patient request routing | Handle patient cases step by step through triage, doctor, and specialist                                                |
| **Command**                 | Medical actions         | Execute and undo commands like prescribing or cancelling medications                                                    |
| **Mediator**                | Hospital departments    | Coordinate communication among departments (doctor ↔ pharmacy ↔ billing)                                                |
| **Memento**                 | Patient records         | Save and restore previous versions of a patient’s diagnosis/treatment                                                   |
| **Observer**                | Notification system     | Notify observers (relatives, billing, pharmacy) when a patient’s status changes                                         |
| **Visitor**                 | Reports/Analytics       | Add new operations (like generating reports or applying discounts) to existing hospital entities without modifying them |


### 🏗️ System Overview

Major Components:

    - Patient Intake and Triage (Chain of Responsibility)
    - Doctor Actions (Command + Memento)
    - Department Coordination (Mediator)
    - Notifications to Relatives and Services (Observer)
    - Report Generation (Visitor)

### 🧩 How the Patterns Work Together

| Pattern                     | Role in Workflow                                             |
| --------------------------- | ------------------------------------------------------------ |
| **Chain of Responsibility** | Routes patients through triage → doctor → specialist         |
| **Command + Memento**       | Handles treatment actions and rollback capability            |
| **Mediator**                | Coordinates inter-departmental communication                 |
| **Observer**                | Updates relatives and systems about patient status           |
| **Visitor**                 | Generates analytics/reports without changing data structures |
