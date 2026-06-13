import streamlit as st
import pandas as pd
from queries import get_all_opportunities  # Adjust based on your queries.py

st.set_page_config(page_title="View & Search Opportunities", page_icon="🔍", layout="wide")

if not st.session_state.get("authenticated", False):
    st.warning("Please login from the Home page first.")
else:
    st.title("🔍 View & Search Opportunities")
    st.markdown("---")

    # Sidebar Filters
    st.sidebar.header("Filter Results")
    search_term = st.sidebar.text_input("Search Job Title / Company")
    f_category = st.sidebar.multiselect("Category", ["Data Science", "AI", "Web Development", "Cyber Security", "Software Engineering"])
    f_mode = st.sidebar.multiselect("Work Mode", ["Onsite", "Remote", "Hybrid"])
    f_status = st.sidebar.selectbox("Status", ["All", "Open", "Closed", "Expired", "Shortlisted"])

    try:
        # Fetching data into DataFrame
        df = get_all_opportunities()
        
        if not df.empty:
            # Apply dynamic filtering in Pandas
            if search_term:
                df = df[df['company_name'].str.contains(search_term, case=False) | df['job_title'].str.contains(search_term, case=False)]
            if f_category:
                df = df[df['category'].isin(f_category)]
            if f_mode:
                df = df[df['work_mode'].isin(f_mode)]
            if f_status != "All":
                df = df[df['status'] == f_status]
            
            st.metric(label="Total Opportunities Found", value=len(df))
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No records found in the database.")
    except Exception as e:
        st.error(f"Error loading data: {e}")