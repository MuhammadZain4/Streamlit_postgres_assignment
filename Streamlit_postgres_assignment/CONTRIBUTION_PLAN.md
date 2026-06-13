# Streamlit PostgreSQL Assignment Contribution Plan

## Repository
`https://github.com/MuhammadZain4/Streamlit_postgres_assignment.git`

## 1. Complete implementation plan

### Member 1: MuhammadZain4
- `database/init.sql` — define PostgreSQL schema for `opportunities`
- `database/seed_data.sql` — add seeded sample records
- `.env.example` — document database environment variables
- `app/db.py` — implement SQLAlchemy engine, connection pooling, health check helper
- `app/queries.py` — implement database query layer for CRUD, search, bulk import, and logging

### Member 2: Nabeelarshad381
- `app/main.py` — implement Streamlit landing page, authentication sidebar, and app overview
- `app/auth.py` — implement login/logout/session and role-based access control
- `app/pages/1_Add_Opportunity.py` — create add opportunity form and validation
- `app/pages/2_View_Search.py` — create view and search page with filters
- `app/pages/3_Update_Opportunity.py` — create update page for status and opportunity fields
- `app/pages/4_Delete_Opportunity.py` — create delete page with confirmation workflow

### Member 3: Raziudinn
- `app/pages/5_Analytics_Dashboard.py` — create analytics dashboard and summary charts
- `app/pages/6_CSV_Upload_Export.py` — create CSV upload/export and bulk load support
- `app/pages/7_Duplicate_Detection.py` — implement duplicate detection page
- `app/pages/8_Deadline_Alerts.py` — implement application deadline alerts and reminders
- `app/pages/9_Database_Health_Check.py` — implement database connectivity and health checks
- `Dockerfile` — containerize Streamlit app
- `docker-compose.yml` — compose PostgreSQL, pgAdmin, and Streamlit services
- `README.md` — add usage, setup, and deployment documentation
- `screenshots/` — add demo screenshots and evidence of working app

## 2. 7–10 realistic commits for each member

### Member 1 commits
1. `db: add initial PostgreSQL schema for internship/job opportunities`
2. `db: add seed data for sample internship and job records`
3. `config: add .env.example with PostgreSQL environment variables`
4. `db: implement SQLAlchemy engine and cached connection in app/db.py`
5. `db: add database health check helper to app/db.py`
6. `queries: add fetch and search helper functions in app/queries.py`
7. `queries: add insert/create helper with default values and validation`
8. `queries: add update, delete, and bulk insert helper functions`
9. `queries: add logging and error handling for database operations`

### Member 2 commits
1. `ui: add Streamlit home page and sidebar authentication guidance`
2. `auth: implement login, logout, and role session helpers`
3. `feature: add add-opportunity page with form validation`
4. `feature: add view/search page with dynamic filters and results`
5. `feature: add update page for opportunity status and work mode`
6. `feature: add delete page with confirmation workflow`
7. `integration: connect CRUD pages to backend query layer`
8. `ui: add admin-only access enforcement on CRUD pages`
9. `ui: improve feedback and error handling in CRUD pages`

### Member 3 commits
1. `analytics: add dashboard page with summary metrics and charts`
2. `feature: add CSV upload/export page and bulk import workflow`
3. `feature: add duplicate detection page`
4. `feature: add deadline alert and reminder page`
5. `feature: add database health check UI`
6. `docker: add Dockerfile for Streamlit application container`
7. `docker: add docker-compose.yml for postgres, pgAdmin, and Streamlit`
8. `docs: add README installation and usage instructions`
9. `docs: add screenshots folder for demo evidence`

## 3. Pull request sequence
1. Member 1: `feature/db-backend`
2. Member 2: `feature/auth-home`
3. Member 2: `feature/crud-pages`
4. Member 3: `feature/analytics-csv`
5. Member 3: `feature/deployment-docs`

## 4. Development order
1. Build backend database and query API (Member 1)
2. Build authentication and core CRUD UI (Member 2)
3. Build analytics, CSV/export, alerts, and health checks (Member 3)
4. Add deployment and documentation support (Member 3)

## 5. Tasks that may cause merge conflicts
- `app/queries.py` — shared backend API names and query helpers
- `app/main.py` — page flow or sidebar changes
- `README.md` — documentation updates from multiple members
- `.env.example` — environment variable naming changes
- `Dockerfile` / `docker-compose.yml` — deployment settings
- `app/db.py` — connection string or helper naming changes

## 6. Git commands each member should run

### Shared setup
```bash
git clone https://github.com/MuhammadZain4/Streamlit_postgres_assignment.git
cd Streamlit_postgres_assignment
git checkout main
git pull origin main
```

### Member 1
```bash
git checkout -b feature/db-backend
git add database/init.sql database/seed_data.sql app/db.py app/queries.py .env.example
git commit -m "db: add initial PostgreSQL schema for internship/job opportunities"
git push -u origin feature/db-backend
```

### Member 2
```bash
git checkout main
git pull origin main
git checkout -b feature/auth-home
git add app/main.py app/auth.py
git commit -m "ui: add Streamlit landing page and authentication helpers"
git push -u origin feature/auth-home
```

```bash
git checkout main
git pull origin main
git checkout -b feature/crud-pages
git add app/pages/1_Add_Opportunity.py app/pages/2_View_Search.py app/pages/3_Update_Opportunity.py app/pages/4_Delete_Opportunity.py
git commit -m "feature: add CRUD pages for opportunity management"
git push -u origin feature/crud-pages
```

### Member 3
```bash
git checkout main
git pull origin main
git checkout -b feature/analytics-csv
git add app/pages/5_Analytics_Dashboard.py app/pages/6_CSV_Upload_Export.py app/pages/7_Duplicate_Detection.py app/pages/8_Deadline_Alerts.py app/pages/9_Database_Health_Check.py
git commit -m "analytics: add dashboard, CSV import/export, duplicate detection, and deadline alerts"
git push -u origin feature/analytics-csv
```

```bash
git checkout main
git pull origin main
git checkout -b feature/deployment-docs
git add Dockerfile docker-compose.yml README.md screenshots
git commit -m "docs: add Docker compose deployment and README setup instructions"
git push -u origin feature/deployment-docs
```

## 7. Professional commit message guidance
- Use present-tense verbs
- Keep scope tags like `db:`, `auth:`, `feature:`, `docs:`, `docker:`
- Keep messages concise but descriptive
- Mention the exact feature or file group changed

## Notes
- Use `git fetch origin` and `git rebase origin/main` before opening each PR.
- Keep each PR narrowly focused on one feature set.
- Review integration with backend before merging UI pages.
