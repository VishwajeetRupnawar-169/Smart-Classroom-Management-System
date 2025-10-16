🎓 AI-Powered Timetable & Smart Attendance Management System

A full-stack intelligent classroom management solution integrating AI-based face recognition attendance, automated timetable generation, real-time analytics, and multi-system data integration (Leave, Payroll, Finance, and Calendar systems).

🧠 Overview

This project revolutionizes academic administration by combining Computer Vision, AI-driven Scheduling, and Cloud Integration to automate the entire lifecycle of attendance and timetable management.
Built for scalability, it supports multi-camera classrooms, real-time facial tracking, absence detection timers, and automated Google/Outlook calendar updates for faculty and students.

🚀 Key Features
🧍‍♂️ Smart Attendance System

Multi-camera face recognition using YOLOv8 + FaceNet for real-time tracking.

Absence Timer Logic: Marks students temporarily or permanently absent after inactivity.

Session-wise attendance synced with live timetables.

Auto sheet creation and Excel synchronization.

🗓️ Automated Timetable Generation

Genetic Algorithm-based timetable optimization in Django backend.

Conflict-free scheduling for teachers, rooms, and subjects.

Dynamic constraint handling (preferences, availability, department limits).

Auto-update to Google Calendar & Outlook.

📊 Data Visualization & Analytics

Real-time dashboards using React + Recharts + D3.js.

Attendance insights, faculty utilization, and class performance analytics.

💼 Enterprise Integration

Linked with Leave Management, Payroll, and Finance systems.

Exports data to Excel, PDF, or cloud dashboards.

🔒 Security & Reliability

JWT-based authentication with role-based access (Admin, Teacher, Student).

MongoDB Atlas with SSL and field-level encryption.

Background tasks handled via Celery + Redis.

🧩 System Architecture
flowchart TD
A[Frontend - React + Vite] --> B[Flask API Gateway]
B --> C[Django Timetable Service]
B --> D[Face Recognition Service - OpenCV + YOLOv8 + FaceNet]
B --> E[MongoDB Atlas - Lecture Metadata & Attendance]
C --> F[Google Calendar API]
C --> G[Outlook Integration]
E --> H[Analytics Engine - Pandas + Matplotlib]
H --> I[Visualization Dashboard]
D --> J[Camera Streams (C1, C2)]

🛠️ Tech Stack
Frontend

React 18

Vite 5

Tailwind CSS 3.4

ShadCN/UI + Lucide Icons

Recharts / D3.js for analytics

Backend

Flask 3.0 – API Gateway

Django 5.0 – Automated Timetable Generation (Genetic Algorithm)

Celery 5.3 + Redis – Task Scheduling

Python 3.11

AI / ML Layer

OpenCV 4.10

YOLOv8 (Ultralytics) – Face Detection

FaceNet / DeepFace – Face Recognition

PyTorch 2.3 – Model Training

MediaPipe – Pose Keypoints

LayoutLMv3 – Document Intelligence (for financial PDFs)

Database

MongoDB Atlas 7.0 – Attendance & Lecture Metadata

PostgreSQL 16 – Timetable Data

Redis – Caching & Background Tasks

Cloud & Integrations

Google Cloud Storage / Drive API

Microsoft Outlook Calendar API

Docker + Kubernetes for deployment

Nginx reverse proxy

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/yourusername/ai-timetable-attendance.git
cd ai-timetable-attendance

2️⃣ Backend Setup
cd backend
pip install -r requirements.txt
flask run

3️⃣ Frontend Setup
cd frontend
npm install
npm run dev

4️⃣ Environment Configuration

Create .env files for both Flask and Django:

MONGO_URI=
REDIS_URL=
GOOGLE_CALENDAR_CREDENTIALS=
OUTLOOK_CLIENT_ID=
SECRET_KEY=

📈 Data Flow

Face Recognition Pipeline:
Captures video feed → detects faces → recognizes identity → logs session attendance → updates MongoDB.

Timetable Generation:
Reads faculty, subjects, rooms → applies Genetic Algorithm → produces optimized timetable → syncs to Google/Outlook.

Integration Layer:
Connects attendance with payroll, leave, and calendar APIs for unified reporting.

🧩 Modules
Module	Description
Face Recognition Service	Handles real-time video feeds using YOLOv8 + FaceNet.
Timetable Engine	Genetic Algorithm in Django for scheduling optimization.
Data Sync Layer	Manages communication between Flask API and MongoDB.
Visualization Dashboard	React-based analytics portal for admins.
Integration Hub	Connects external services like Google Calendar and Payroll.
📷 Demo Snapshots

(Add screenshots or gifs of dashboard, attendance marking, and timetable view here)

🧪 Testing
pytest tests/

📚 Future Enhancements

Multilingual Voice Alerts for absent students.

AI-powered timetable conflict prediction.

Integration with biometric systems.

Federated Face Recognition for privacy-preserving attendance.

👨‍💻 Contributors

Vishwajeet Baban Rupnawar – Project Lead & AI Engineer
📧 [vishwajeet.rupnawar@rscoe.edu.in
]
💼 AICTE Edunet Techsakham | Gen AI Intern

🏆 License

MIT License © 2025 Vishwajeet Baban Rupnawar
