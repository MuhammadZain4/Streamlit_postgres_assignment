import streamlit as st
import pandas as pd
from db import get_db_engine  # Adjust import paths based on your actual db.py setup
from sqlalchemy import text

st.set_page_config(page_title="Database Health Check", page_icon="🏥", layout="wide")

if not st.session_state.get("authenticated", False):
    st.warning("Please login from the Home page first.")
else:
    st.title("🏥 PostgreSQL Database Health & Schema Metrics")
    st.markdown("---")

    try:
        engine = get_db_engine()
        with engine.connect() as conn:
            # 1. Test query for version
            version_res = conn.execute(text("SELECT version();")).fetchone()
            # 2. Get Count
            count_res = conn.execute(text("SELECT COUNT(*) FROM opportunities;")).fetchone()
            
            st.success("✅ Connected to PostgreSQL Server Engine Successfully!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Database Connectivity State", "Active & Healthy")
                st.write(f"**PostgreSQL Engine Runtime Spec:** `{version_res[0]}`")
            with col2:
                st.metric("Total Records In Table", count_res[0])
                
            st.markdown("---")
            st.subheader("📋 Core Schema Structure Definitions")
            schema_info = conn.execute(text("""
                SELECT column_name, data_type, is_nullable 
                FROM information_schema.columns 
                WHERE table_name = 'opportunities';
            """)).fetchall()
            
            schema_df = pd.DataFrame(schema_info, columns=["Column Name", "Data Type", "Is Nullable"])
            st.table(schema_df)

    except Exception as e:
        st.error(f"🛑 Health Status Failure: Unable to establish contact with database containers. Details: {e}")