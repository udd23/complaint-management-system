# CampusCare 🚀  
Smart Campus Complaint Management System with SLA-Based Escalation & Accountability

## 📌 Concept
CampusCare is a web-based complaint management and escalation platform designed for college campuses and hostel environments.  
The system provides a structured workflow for students and residents to report issues related to hostel facilities, Wi-Fi, cleanliness, classrooms, and campus security.  

Unlike traditional complaint boxes or informal reporting, CampusCare enforces **accountability through SLA (Service Level Agreement) timelines**, automated routing to responsible authorities, and escalation to higher management in case of inaction. The platform is designed to improve transparency, responsiveness, and operational efficiency in campus administration.

---

## ✨ Key Features

### 🔐 User & Access Management
- Student/hostel resident registration and authentication  
- Role-based access control (Student, Warden/Rector, HOD, Admin)  
- Secure login and session management  

### 📝 Complaint Management
- Complaint submission with category, description, and priority  
- File/image attachment support (optional enhancement)  
- Real-time complaint status tracking  

### 🔁 Workflow & Escalation
- Automatic routing to relevant lower authority based on complaint category  
- 24-hour SLA for initial action by assigned authority  
- Action options for authorities:
  - Resolve  
  - Forward to higher authority (with justification)  
  - Cancel (with valid reason)  
- Automatic escalation on SLA breach  
- Mandatory delay justification on SLA violation  

### 📊 Administration & Transparency
- Admin dashboard with filters and search  
- Audit logs for all status changes and actions  
- Visibility into SLA breaches and escalations  

---

## 🛠 Technology Stack

- **Backend:** Django (Python)  
- **Frontend:** Django Templates (HTML, CSS, JavaScript)  
- **UI Framework:** Bootstrap / Tailwind CSS (optional)  
- **Database:** SQLite (development), PostgreSQL (production-ready)  
- **Authentication & Authorization:** Django Auth (Role-Based Access Control)  
- **Task Scheduling (Future):** Celery / Cron for SLA checks and auto-escalation  

---

## 🔄 Workflow

1. **Complaint Submission**  
   A student or hostel resident submits a complaint with category and priority.

2. **Automatic Routing**  
   The system routes the complaint to the relevant lower authority:
   - Hostel issues → Warden/Rector  
   - Academic issues → HOD  

3. **SLA Enforcement (24 Hours)**  
   The assigned authority must take action within 24 hours:
   - Resolve the complaint  
   - Forward to higher authority (with justification)  
   - Cancel with valid reason  

4. **Auto-Escalation on SLA Breach**  
   If no action is taken within the SLA window:
   - The system automatically escalates the complaint to higher authorities  
   - An SLA breach is logged  
   - The lower authority must provide a mandatory justification  

5. **Final Resolution & Closure**  
   Higher authorities review escalated complaints and ensure final resolution.  
   All actions and state transitions are recorded in audit logs for transparency and accountability.

---

## 🎯 Objective
CampusCare aims to replace informal and ineffective grievance mechanisms with a **structured, auditable, and SLA-driven digital system** that improves campus governance, accountability, and service quality.

> This project is built as a real-world workflow system for learning, portfolio demonstration, and potential pilot deployment in educational institutions.


## 👤 Author

**Name:** Uday Sapkale
**Role:** B.Tech IT Student | Full-Stack (Django) Developer  
**GitHub:** https://github.com/wbu_ud
**LinkedIn:** https://www.linkedin.com/in/uday-sapkale/  
**Email:** udaysapkale109@gmail.com

> Passionate about building real-world workflow systems and scalable web applications.
