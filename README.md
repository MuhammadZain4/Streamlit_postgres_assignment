# Student Internship & Job Tracking System

An integrated full-stack web application designed for university faculty members to seamlessly coordinate, manage, and audit student internship and job placement records while tracking modern industrial hiring trends.

## 🚀 Tech Stack & Architecture
- **Frontend UI:** Streamlit (Multipage Framework)
- **Database Server:** PostgreSQL (Relational Database)
- **Data Persistence:** Docker Volumes (`postgres_data`)
- **DB Administration:** pgAdmin 4 (Web Interface Container)
- **Orchestration Layer:** Docker Compose (Multi-Container Network)

## 📁 Project Structure
```text
streamlit-postgres-assignment/
├── app/
│   ├── pages/
│   │   ├── 1_Add_Opportunity.py
│   │   ├── 2_View_Search.py
│   │   ├── 3_Update_Opportunity.py
│   │   ├── 4_Delete_Opportunity.py
│   │   ├── 5_Analytics_Dashboard.py
│   │   ├── 6_CSV_Upload_Export.py
│   │   ├── 7_Duplicate_Detection.py
│   │   ├── 8_Deadline_Alert.py
│   │   └── 9_Database_Health_Check.py
│   ├── auth.py
│   ├── db.py
│   ├── main.py
│   └── queries.py
├── database/
│   ├── init.sql
│   └── seed_data.sql
├── .env
├── Dockerfile
├── docker-compose.yml
└── requirements.txt

🛠️ How to Run the Project
Prerequisites
Make sure you have Docker and Docker Desktop installed on your system.

Step 1: Clone and Configure
Clone this repository to your local machine.

Ensure your .env file is configured with the correct PostgreSQL credentials.

Step 2: Build and Launch Containers
Open your terminal inside the project root directory and run:

Bash
docker compose up --build -d

Step 3: Access the Applications
Streamlit Web UI: Open http://localhost:8501 in your browser.

pgAdmin 4 Dashboard: Open http://localhost:5050 to manage the database visually.

Step 4: Stop Containers
To securely spin down the containers without deleting data, run:

Bash
docker compose down