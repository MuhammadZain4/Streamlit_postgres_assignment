import streamlit as st
import pandas as pd
import datetime
from queries import get_all_opportunities  # Adjust based on queries.py

st.set_page_config(page_title="Deadline Alerts", page_icon="⏰", layout="wide")

if not st.session_state.get("authenticated", False):
    st.warning("Please login from the Home page first.")
else:
    st.title("⏰ Urgent Deadline Alerts & Monitoring")
    st.markdown("---")

    try:
        df = get_all_opportunities()
        if not df.empty:
            # Convert string dates to datetime objects if needed safely
            df['application_deadline'] = pd.to_datetime(df['application_deadline']).dt.date
            today = datetime.date.today()
            seven_days_later = today + datetime.timedelta(days=7)

            # 1. Closing soon within 7 days
            closing_soon = df[(df['application_deadline'] >= today) & (df['application_deadline'] <= seven_days_later) & (df['status'] == 'Open')]
            
            # 2. Already Expired records
            expired_jobs = df[(df['application_deadline'] < today) | (df['status'] == 'Expired')]

            st.subheader("🔥 Closing Within Next 7 Days")
            if not closing_soon.empty:
                st.error(f"The following {len(closing_soon)} active opportunities are reaching their limit immediately:")
                st.dataframe(closing_soon[['opportunity_id', 'company_name', 'job_title', 'application_deadline', 'status']], use_container_width=True)
            else:
                st.success("No active jobs are closing within the next 7 days.")

            st.markdown("---")
            st.subheader("⚠️ Expired / Historical Records")
            if not expired_jobs.empty:
                st.info(f"There are {len(expired_jobs)} outdated roles tracked here:")
                st.dataframe(expired_jobs[['opportunity_id', 'company_name', 'job_title', 'application_deadline', 'status']], use_container_width=True)
        else:
            st.info("No records to evaluate deadlines.")
    except Exception as e:
        st.error(f"Error parsing dates: {e}")