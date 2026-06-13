"""
queries.py — All database query functions
Uses SQLAlchemy engine from db.py.
Every function returns plain Python objects (dicts, lists, DataFrames).
"""

import pandas as pd
from datetime import date, timedelta
from sqlalchemy import text
import logging

# Standard logging configuration
logging.basicConfig(level=logging.INFO)

from db import get_db_engine

# Helper to maintain compatibility if get_engine is called anywhere
get_engine = get_db_engine

# ══════════════════════════════════════════════════════════════
# READ
# ══════════════════════════════════════════════════════════════

def fetch_all_opportunities() -> pd.DataFrame:
    """Return every row as a DataFrame."""
    sql = "SELECT * FROM opportunities ORDER BY created_at DESC"
    with get_db_engine().connect() as conn:
        return pd.read_sql(text(sql), conn)


def fetch_opportunity_by_id(opp_id: int) -> pd.DataFrame:
    sql = "SELECT * FROM opportunities WHERE opportunity_id = :id"
    with get_db_engine().connect() as conn:
        return pd.read_sql(text(sql), conn, params={"id": opp_id})


def search_opportunities(
    keyword: str = "",
    category: str = "",
    city: str = "",
    work_mode: str = "",
    status: str = "",
    salary_min: float = 0,
    salary_max: float = 9_999_999,
    experience_level: str = "",
) -> pd.DataFrame:
    """
    Flexible search with multiple optional filters.
    keyword matches company_name, job_title, or required_skills.
    """
    conditions = ["1=1"]
    params: dict = {}

    if keyword:
        conditions.append(
            "(company_name ILIKE :kw OR job_title ILIKE :kw OR required_skills ILIKE :kw)"
        )
        params["kw"] = f"%{keyword}%"
    if category:
        conditions.append("category = :category")
        params["category"] = category
    if city:
        conditions.append("city ILIKE :city")
        params["city"] = f"%{city}%"
    if work_mode:
        conditions.append("work_mode = :work_mode")
        params["work_mode"] = work_mode
    if status:
        conditions.append("status = :status")
        params["status"] = status
    if salary_min:
        conditions.append("salary_min >= :sal_min")
        params["sal_min"] = salary_min
    if salary_max < 9_999_999:
        conditions.append("salary_max <= :sal_max")
        params["sal_max"] = salary_max
    if experience_level:
        conditions.append("experience_level = :exp")
        params["exp"] = experience_level

    sql = f"SELECT * FROM opportunities WHERE {' AND '.join(conditions)} ORDER BY created_at DESC"
    with get_db_engine().connect() as conn:
        return pd.read_sql(text(sql), conn, params=params)


# ══════════════════════════════════════════════════════════════
# CREATE
# ══════════════════════════════════════════════════════════════

def insert_opportunity(*args, **kwargs):
    engine = get_db_engine()
    if args:
        params = {
            "company_name": args[0] if len(args) > 0 else None,
            "job_title": args[1] if len(args) > 1 else None,
            "category": args[2] if len(args) > 2 else None,
            "city": args[3] if len(args) > 3 else None,
            "country": args[4] if len(args) > 4 else None,
            "work_mode": args[5] if len(args) > 5 else None,
            "required_skills": args[6] if len(args) > 6 else "",
            "salary_min": args[7] if len(args) > 7 else 0.0,
            "salary_max": args[8] if len(args) > 8 else 0.0,
            "currency": args[9] if len(args) > 9 else 'PKR',
            "application_deadline": args[10] if len(args) > 10 else None,
            "experience_level": args[11] if len(args) > 11 else 'Entry Level',
            "status": args[12] if len(args) > 12 else 'Open',
            "source_link": args[13] if len(args) > 13 else None,
        }
    else:
        params = {
            "company_name": kwargs.get("company_name"),
            "job_title": kwargs.get("job_title"),
            "category": kwargs.get("category", "Data Science"),
            "city": kwargs.get("city", "Lahore"),
            "country": kwargs.get("country", "Pakistan"),
            "work_mode": kwargs.get("work_mode", "Onsite"),
            "required_skills": kwargs.get("required_skills", ""),
            "salary_min": kwargs.get("salary_min", 0.0),
            "salary_max": kwargs.get("salary_max", 0.0),
            "currency": kwargs.get("currency", "PKR"),
            "application_deadline": kwargs.get("application_deadline"),
            "experience_level": kwargs.get("experience_level", "Entry Level"),
            "status": kwargs.get("status", "Open"),
            "source_link": kwargs.get("source_link", None)
        }

    sql = """
    INSERT INTO opportunities (
        company_name, job_title, category, city, country, work_mode, 
        required_skills, salary_min, salary_max, currency, experience_level, 
        application_deadline, status, source_link
    ) VALUES (
        :company_name, :job_title, :category, :city, :country, :work_mode, 
        :required_skills, :salary_min, :salary_max, :currency, :experience_level, 
        :application_deadline, :status, :source_link
    );
    """
    try:
        with engine.begin() as conn:
            conn.execute(text(sql), params)
        return True
    except Exception as e:
        logging.error(f"Error inserting opportunity: {e}")
        raise e


def get_all_opportunities():
    """Fetches all records from the database and returns them as a Pandas DataFrame."""
    engine = get_db_engine()
    sql = "SELECT * FROM opportunities ORDER BY created_at DESC;"
    try:
        with engine.connect() as conn:
            df = pd.read_sql(text(sql), conn)
        # Ensure 'opportunity_id' maps seamlessly across components if any script looks for standard '.id'
        if not df.empty and 'opportunity_id' in df.columns:
            df['id'] = df['opportunity_id']
        return df
    except Exception as e:
        logging.error(f"Error fetching opportunities: {e}")
        return pd.DataFrame()


def bulk_insert_opportunities(rows: list[dict]) -> tuple[int, list[str]]:
    success = 0
    errors  = []
    sql = text("""
        INSERT INTO opportunities (
            company_name, job_title, category, city, country, work_mode,
            required_skills, salary_min, salary_max, currency,
            experience_level, application_deadline, status, source_link
        ) VALUES (
            :company_name, :job_title, :category, :city, :country, :work_mode,
            :required_skills, :salary_min, :salary_max, :currency,
            :experience_level, :application_deadline, :status, :source_link
        )
    """)
    with get_db_engine().begin() as conn:
        for i, row in enumerate(rows):
            try:
                conn.execute(sql, row)
                success += 1
            except Exception as exc:
                errors.append(f"Row {i + 1}: {exc}")
    return success, errors


# ══════════════════════════════════════════════════════════════
# UPDATE
# ══════════════════════════════════════════════════════════════

def update_opportunity(opp_id: int, data: dict) -> bool:
    if not data:
        return False

    set_clauses = ", ".join(f"{k} = :{k}" for k in data)
    data["opp_id"] = opp_id
    sql = text(f"UPDATE opportunities SET {set_clauses} WHERE opportunity_id = :opp_id")

    with get_db_engine().begin() as conn:
        result = conn.execute(sql, data)
        return result.rowcount > 0


def update_opportunity_status(*args, **kwargs):
    """Handles multiple arguments dynamically for the status and work mode page updates using opportunity_id."""
    engine = get_db_engine()
    opportunity_id = args[0] if len(args) > 0 else kwargs.get("opportunity_id")
    new_status = args[1] if len(args) > 1 else kwargs.get("new_status")
    new_work_mode = args[2] if len(args) > 2 else kwargs.get("new_work_mode")

    if not opportunity_id:
        opportunity_id = kwargs.get("id") or kwargs.get("opp_id")
    if not new_status and "status" in kwargs:
        new_status = kwargs.get("status")
    if not new_work_mode and "work_mode" in kwargs:
        new_work_mode = kwargs.get("work_mode")

    try:
        with engine.begin() as conn:
            if new_status and new_work_mode:
                sql = "UPDATE opportunities SET status = :status, work_mode = :work_mode WHERE opportunity_id = :id;"
                conn.execute(text(sql), {"status": new_status, "work_mode": new_work_mode, "id": opportunity_id})
            elif new_work_mode:
                sql = "UPDATE opportunities SET work_mode = :work_mode WHERE opportunity_id = :id;"
                conn.execute(text(sql), {"work_mode": new_work_mode, "id": opportunity_id})
            else:
                sql = "UPDATE opportunities SET status = :status WHERE opportunity_id = :id;"
                conn.execute(text(sql), {"status": new_status, "id": opportunity_id})
        return True
    except Exception as e:
        logging.error(f"Error updating opportunity: {e}")
        raise e


# ══════════════════════════════════════════════════════════════
# DELETE
# ══════════════════════════════════════════════════════════════

def delete_opportunity(opp_id: int) -> bool:
    """Delete a single record by ID matching database primary key opportunity_id."""
    sql = text("DELETE FROM opportunities WHERE opportunity_id = :id")
    with get_db_engine().begin() as conn:
        result = conn.execute(sql, {"id": opp_id})
        return result.rowcount > 0


# ══════════════════════════════════════════════════════════════
# DUPLICATE DETECTION
# ══════════════════════════════════════════════════════════════

def find_duplicates() -> pd.DataFrame:
    sql = text("""
        SELECT
            company_name,
            job_title,
            city,
            source_link,
            COUNT(*) AS duplicate_count,
            ARRAY_AGG(opportunity_id ORDER BY opportunity_id) AS ids,
            MIN(created_at) AS first_created
        FROM opportunities
        GROUP BY company_name, job_title, city, source_link
        HAVING COUNT(*) > 1
        ORDER BY duplicate_count DESC
    """)
    with get_db_engine().connect() as conn:
        return pd.read_sql(sql, conn)


def check_duplicate_before_insert(company: str, title: str, city: str, link: str) -> bool:
    sql = text("""
        SELECT COUNT(*) FROM opportunities
        WHERE company_name ILIKE :company
          AND job_title    ILIKE :title
          AND city         ILIKE :city
    """)
    params = {"company": company, "title": title, "city": city}
    with get_db_engine().connect() as conn:
        count = conn.execute(sql, params).scalar()
    return count > 0


# ══════════════════════════════════════════════════════════════
# DEADLINE ALERTS
# ══════════════════════════════════════════════════════════════

def fetch_closing_soon(days: int = 7) -> pd.DataFrame:
    target = date.today() + timedelta(days=days)
    sql = text("""
        SELECT opportunity_id, company_name, job_title, category,
               city, work_mode, application_deadline, status
        FROM opportunities
        WHERE status = 'Open'
          AND application_deadline BETWEEN CURRENT_DATE AND :target
        ORDER BY application_deadline ASC
    """)
    with get_db_engine().connect() as conn:
        return pd.read_sql(sql, conn, params={"target": target})


def fetch_expired() -> pd.DataFrame:
    sql = text("""
        SELECT opportunity_id, company_name, job_title, category,
               city, application_deadline, status
        FROM opportunities
        WHERE application_deadline < CURRENT_DATE
          AND status NOT IN ('Closed', 'Expired')
        ORDER BY application_deadline ASC
    """)
    with get_db_engine().connect() as conn:
        return pd.read_sql(sql, conn)


# ══════════════════════════════════════════════════════════════
# ANALYTICS / DASHBOARD METRICS
# ══════════════════════════════════════════════════════════════

def fetch_kpis() -> dict:
    with get_db_engine().connect() as conn:
        total       = conn.execute(text("SELECT COUNT(*) FROM opportunities")).scalar()
        open_count  = conn.execute(text("SELECT COUNT(*) FROM opportunities WHERE status='Open'")).scalar()
        closed      = conn.execute(text("SELECT COUNT(*) FROM opportunities WHERE status='Closed'")).scalar()
        shortlisted = conn.execute(text("SELECT COUNT(*) FROM opportunities WHERE status='Shortlisted'")).scalar()
        companies   = conn.execute(text("SELECT COUNT(DISTINCT company_name) FROM opportunities")).scalar()
        avg_salary  = conn.execute(
            text("SELECT ROUND(AVG((salary_min+salary_max)/2),0) FROM opportunities WHERE currency='PKR'")
        ).scalar()
        closing_soon = conn.execute(
            text("""
                SELECT COUNT(*) FROM opportunities
                WHERE status='Open'
                  AND application_deadline BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '7 days'
            """)
        ).scalar()
        remote_count = conn.execute(
            text("SELECT COUNT(*) FROM opportunities WHERE work_mode='Remote'")
        ).scalar()
    return {
        "total":        total,
        "open":         open_count,
        "closed":       closed,
        "shortlisted":  shortlisted,
        "companies":    companies,
        "avg_salary":   avg_salary,
        "closing_soon": closing_soon,
        "remote":       remote_count,
    }


def fetch_by_category() -> pd.DataFrame:
    sql = text("SELECT category, COUNT(*) AS count FROM opportunities GROUP BY category ORDER BY count DESC")
    with get_db_engine().connect() as conn:
        return pd.read_sql(sql, conn)


def fetch_by_status() -> pd.DataFrame:
    sql = text("SELECT status, COUNT(*) AS count FROM opportunities GROUP BY status ORDER BY count DESC")
    with get_db_engine().connect() as conn:
        return pd.read_sql(sql, conn)


def fetch_by_work_mode() -> pd.DataFrame:
    sql = text("SELECT work_mode, COUNT(*) AS count FROM opportunities GROUP BY work_mode")
    with get_db_engine().connect() as conn:
        return pd.read_sql(sql, conn)


def fetch_by_city() -> pd.DataFrame:
    sql = text("SELECT city, COUNT(*) AS count FROM opportunities GROUP BY city ORDER BY count DESC LIMIT 10")
    with get_db_engine().connect() as conn:
        return pd.read_sql(sql, conn)


def fetch_salary_by_category() -> pd.DataFrame:
    sql = text("""
        SELECT category,
               ROUND(AVG(salary_min), 0) AS avg_min,
               ROUND(AVG(salary_max), 0) AS avg_max
        FROM opportunities
        WHERE currency = 'PKR'
          AND salary_min IS NOT NULL
        GROUP BY category
        ORDER BY avg_max DESC
    """)
    with get_db_engine().connect() as conn:
        return pd.read_sql(sql, conn)


def fetch_monthly_postings() -> pd.DataFrame:
    sql = text("""
        SELECT TO_CHAR(created_at, 'YYYY-MM') AS month,
               COUNT(*) AS count
        FROM opportunities
        GROUP BY month
        ORDER BY month ASC
    """)
    with get_db_engine().connect() as conn:
        return pd.read_sql(sql, conn)


def fetch_top_skills(top_n: int = 15) -> pd.DataFrame:
    sql = text("SELECT required_skills FROM opportunities")
    with get_db_engine().connect() as conn:
        df = pd.read_sql(sql, conn)

    from collections import Counter
    skill_counter: Counter = Counter()
    for skills_str in df["required_skills"].dropna():
        for skill in skills_str.split(","):
            s = skill.strip()
            if s:
                skill_counter[s] += 1

    top = skill_counter.most_common(top_n)
    return pd.DataFrame(top, columns=["skill", "count"])


def fetch_experience_distribution() -> pd.DataFrame:
    sql = text("""
        SELECT experience_level, COUNT(*) AS count
        FROM opportunities
        WHERE experience_level IS NOT NULL
        GROUP BY experience_level
        ORDER BY count DESC
    """)
    with get_db_engine().connect() as conn:
        return pd.read_sql(sql, conn)


# ══════════════════════════════════════════════════════════════
# HELPER — dropdown options
# ══════════════════════════════════════════════════════════════

def fetch_distinct(column: str) -> list[str]:
    sql = text(f"SELECT DISTINCT {column} FROM opportunities WHERE {column} IS NOT NULL ORDER BY 1")
    with get_db_engine().connect() as conn:
        rows = conn.execute(sql).fetchall()
    return [r[0] for r in rows]


# Aliases for backward compatibility across multipages
get_all_opportunities = get_all_opportunities
get_opportunities = get_all_opportunities
view_opportunities = get_all_opportunities