"""
db.py — Database connection layer
SQLAlchemy engine with connection pooling, cached via st.cache_resource.
All other modules import get_engine() from here.
"""

import os
import streamlit as st
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()


def _build_connection_string() -> str:
    host     = os.environ.get("DB_HOST",     "localhost")
    port     = os.environ.get("DB_PORT",     "5432")
    name     = os.environ.get("DB_NAME",     "student_opportunities_db")
    user     = os.environ.get("DB_USER",     "app_user")
    password = os.environ.get("DB_PASSWORD", "app_password")
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"


@st.cache_resource(show_spinner="Connecting to database…")
def get_engine():
    """
    Returns a cached SQLAlchemy Engine with a connection pool.
    Called once per Streamlit session; reused across all pages.
    """
    conn_str = _build_connection_string()
    engine = create_engine(
        conn_str,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,   # checks connection health before use
        pool_recycle=300,     # recycle connections every 5 minutes
        echo=False,
    )
    # Validate the connection immediately
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return engine


def test_connection() -> dict:
    """
    Returns a dict with connection status and metadata.
    Used by the Database Health Check page.
    """
    try:
        engine = get_engine()
        with engine.connect() as conn:
            version  = conn.execute(text("SELECT version()")).scalar()
            db_name  = conn.execute(text("SELECT current_database()")).scalar()
            row_count = conn.execute(
                text("SELECT COUNT(*) FROM opportunities")
            ).scalar()
            latest = conn.execute(
                text(
                    "SELECT company_name, job_title, created_at "
                    "FROM opportunities ORDER BY created_at DESC LIMIT 1"
                )
            ).fetchone()
            columns = conn.execute(
                text(
                    "SELECT column_name, data_type "
                    "FROM information_schema.columns "
                    "WHERE table_name = 'opportunities' "
                    "ORDER BY ordinal_position"
                )
            ).fetchall()
        return {
            "status":     "connected",
            "version":    version,
            "db_name":    db_name,
            "row_count":  row_count,
            "latest":     latest,
            "columns":    columns,
        }
    except Exception as exc:
        return {"status": "error", "message": str(exc)}
# File ke bilkul aakhir mein ye line chipka do:
get_db_engine = get_engine