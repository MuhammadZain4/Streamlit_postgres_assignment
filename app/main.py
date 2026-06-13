import streamlit as st

# Page configuration - Must be the first Streamlit command
st.set_page_config(
    page_title="Internship & Job Tracking Dashboard",
    page_icon="💼",
    layout="wide"
)

# Initialize session state for authentication if not exists
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None
if "role" not in st.session_state:
    st.session_state.role = None

# Sidebar Authentication / Access Control Layout
st.sidebar.title("🔐 Access Control")

if not st.session_state.authenticated:
    st.sidebar.subheader("Faculty & Viewer Login")
    username = st.sidebar.text_input("Username", placeholder="e.g., zain")
    password = st.sidebar.text_input("Password", type="password", placeholder="Enter password")
    role_input = st.sidebar.selectbox("Select Your Role", ["Viewer", "Admin"])
    
    if st.sidebar.button("Login"):
        if username.strip() != "" and password == "admin123":  # Default assignment password
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.role = role_input
            st.sidebar.success(f"Logged in successfully as {role_input}!")
            st.rerun()
        else:
            st.sidebar.error("Invalid credentials! (Hint: Use password 'admin123')")
else:
    st.sidebar.write(f"🌐 **Welcome, {st.session_state.username}!**")
    st.sidebar.write(f"Current Role: `{st.session_state.role}`")
    st.sidebar.markdown("---")
    if st.sidebar.button("Log Out"):
        st.session_state.authenticated = False
        st.session_state.username = None
        st.session_state.role = None
        st.rerun()

# Main Page Content
st.title("💼 Student Internship & Job Tracking System")
st.markdown("---")

st.markdown("""
### Welcome to the Faculty Management Portal
This integrated web platform allows university faculty members to seamlessly coordinate, manage, and audit student 
internship and job placement records while tracking modern industrial hiring trends.
""")

# Project Details Layout Split
col1, col2 = st.columns(2)

with col1:
    st.subheader("🛠️ System Architecture & Stack")
    st.info("""
    - **Frontend UI:** Streamlit Multipage Framework
    - **Database Server:** PostgreSQL (Relational Database Service)
    - **Data Persistence:** Docker Volumes (`postgres_data`)
    - **DB Administration:** pgAdmin 4 (Web Interface Container)
    - **Orchestration Layer:** Docker Compose Multi-Container Network
    - **Libraries Used:** SQLAlchemy, Pandas, Plotly, python-dotenv, psycopg2-binary
    """)

with col2:
    st.subheader("👥 Academic Information")
    st.success("""
    - **Institution:** University of Central Punjab (UCP)
    - **Department:** Department of Applied Computing & Technologies
    - **Course:** Tools & Techniques for Data Science
    - **Assignment:** Assignment #4 (Reproducible Data Applications)
    - **Access Scope:** 'Admin' account grants full CRUD privileges. 'Viewer' account grants read-only analytics dashboard access.
    """)

st.markdown("---")
st.subheader("📖 Quick Application Guide")
st.markdown("""
1. **Authentication:** Go to the sidebar, type any username, select your role, type `admin123` as the password, and hit **Login**.
2. **Navigation:** Once logged in, Streamlit's sidebar will show the available multipage sections (Add, View, Update, Delete, Dashboard, CSV Tools, etc.).
3. **Role Enforcement:** - **Admin:** Can add new jobs, update status, delete faulty records, and bulk-import CSV data.
    - **Viewer:** Can view/search records, read the interactive analytics graphs, check deadline alarms, and run export files.
""")

st.warning("⚠️ **Important:** Please ensure that you have run `docker compose up --build -d` inside VS Code terminal so that your Streamlit app can reach the PostgreSQL container!")