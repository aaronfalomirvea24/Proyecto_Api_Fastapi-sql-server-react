# Proyecto_Api_Fastapi-sql-server-react
RestoAPI — Restaurant Management System

A full-stack restaurant management platform built with FastAPI, React, and SQL Server.
Live demo: [your-api.railway.app](https://your-api.railway.app)//earring

---

## Features

- **Smart Dashboard** — Real-time overview of dishes and API latency indicators.
- **Digital Menu** — Fluid interface built with React 18 and Tailwind CSS 3.4.
- **Async Backend** — FastAPI-powered for near-instant response times.
- **Robust Database** — Direct SQL Server integration with optimized queries.
- **Interactive Map** — Strategic location display via Google Maps API.
- **JWT Authentication** — Secure role-based access control for staff and admins.

---

## Tech Stack

| Layer     | Technology                     |
|-----------|-------------------------------|
| Frontend  | React 18, Tailwind CSS 3.4    |
| Backend   | FastAPI, Python 3.10+         |
| Database  | SQL Server                    |
| Auth      | JWT (JSON Web Tokens)         |
| Maps      | Google Maps API               |

---

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js v18+
- Active SQL Server instance

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/scripts/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## API Endpoints

| Method | Endpoint         | Description          | Auth Required |
|--------|-----------------|----------------------|---------------|
| POST   | /auth/login     | User login + JWT     | No            |
| GET    | /menu           | List all dishes      | No            |
| POST   | /menu           | Create dish          | Admin         |
| PUT    | /menu/{id}      | Update dish          | Admin         |
| DELETE | /menu/{id}      | Delete dish          | Admin         |
| GET    | /orders         | List all orders      | Yes           |
| POST   | /orders         | Create new order     | Yes           |

---

## Project Structure
restoapi/

├── backend/

│   ├── app.py

│   ├── routes/

│   ├── models/

│   └── requirements.txt

├── frontend/

│   ├── src/

│   └── package.json

└── README.md
