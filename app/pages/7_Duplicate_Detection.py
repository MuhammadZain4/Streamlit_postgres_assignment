import streamlit as st
import pandas as pd
from queries import get_all_opportunities  # Adjust based on queries.py

st.set_page_config(page_title="Duplicate Detection", page_icon="🧬", layout="wide")

if not st.session_state.get("authenticated", False):
    st.warning("Please login from the Home page first.")
else:
    st.title("🧬 Smart Duplicate Detection System")
    st.markdown("---")
    st.info("This algorithmic check scans data based on overlapping values for Company Name, Job Title, and City.")

    try:
        df = get_all_opportunities()
        if not df.empty:
            # Finding matches
            duplicate_mask = df.duplicated(subset=['company_name', 'job_title', 'city'], keep=False)
            duplicates_df = df[duplicate_mask].sort_values(by=['company_name', 'job_title'])
            
            if not duplicates_df.empty:
                st.warning(f"⚠️ Found {len(duplicates_df)} potential duplicate entries in the tracking records:")
                st.dataframe(duplicates_df[['opportunity_id', 'company_name', 'job_title', 'city', 'status', 'created_at']], use_container_width=True)
            else:
                st.success("✅ Clean Database Integrity Status: No duplicate records found.")
        else:
            st.info("No data inside the table to process duplicate verification patterns.")
    except Exception as e:
        st.error(f"Engine Validation Error: {e}")