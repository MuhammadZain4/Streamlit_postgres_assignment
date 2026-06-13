import streamlit as st
import datetime
from queries import insert_opportunity  # Assuming Claude named it this way

st.set_page_config(page_title="Add Opportunity", page_icon="➕", layout="wide")

if not st.session_state.get("authenticated", False):
    st.warning("Please login from the Home page first.")
elif st.session_state.get("role") != "Admin":
    st.error("⛔ Access Denied! Only Faculty Admins can add new opportunities.")
else:
    st.title("➕ Add New Internship or Job Opportunity")
    st.markdown("---")

    with st.form("add_opportunity_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            company = st.text_input("Company Name*")
            title = st.text_input("Job/Internship Title*")
            category = st.selectbox("Category*", ["Data Science", "AI", "Web Development", "Cyber Security", "Software Engineering"])
            work_mode = st.selectbox("Work Mode*", ["Onsite", "Remote", "Hybrid"])
            skills = st.text_area("Required Skills (Comma separated)*")
        
        with col2:
            city = st.text_input("City", value="Lahore")
            country = st.text_input("Country", value="Pakistan")
            sal_min = st.number_input("Minimum Salary", min_value=0.0, step=5000.0)
            sal_max = st.number_input("Maximum Salary", min_value=0.0, step=5000.0)
            currency = st.selectbox("Currency", ["PKR", "USD"])
            deadline = st.date_input("Application Deadline", min_value=datetime.date.today())

        submitted = st.form_submit_button("Submit Opportunity")
        
        if submitted:
            if not company or not title or not skills:
                st.error("Please fill all mandatory fields (*)")
            elif sal_min > sal_max and sal_max > 0:
                st.error("Minimum salary cannot be greater than maximum salary.")
            else:
                try:
                    # Adjust parameters based on your exact app/queries.py structure
                    insert_opportunity(company, title, category, city, country, work_mode, skills, sal_min, sal_max, currency, deadline)
                    st.success(f"🎉 Opportunity for {title} at {company} added successfully!")
                except Exception as e:
                    st.error(f"Database Error: {e}")