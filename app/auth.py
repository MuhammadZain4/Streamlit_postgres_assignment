"""
auth.py — Role-Based Access Control
Two roles: Admin (full CRUD) and Viewer (read-only).
Credentials are intentionally simple for a university demo.
"""

import streamlit as st

# ── Credential store ──────────────────────────────────────────
# In a real system these would come from a hashed DB table.
USERS = {
    "admin":  {"password": "admin123",  "role": "Admin"},
    "viewer": {"password": "viewer123", "role": "Viewer"},
    "faculty": {"password": "faculty123", "role": "Admin"},
}


# ── Helpers ───────────────────────────────────────────────────

def init_session():
    """Initialize session state keys if they don't exist yet."""
    defaults = {
        "logged_in": False,
        "username":  "",
        "role":      "",
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val


def login(username: str, password: str) -> bool:
    """Validate credentials and populate session state."""
    user = USERS.get(username.lower())
    if user and user["password"] == password:
        st.session_state.logged_in = True
        st.session_state.username  = username.lower()
        st.session_state.role      = user["role"]
        return True
    return False


def logout():
    """Clear session state."""
    st.session_state.logged_in = False
    st.session_state.username  = ""
    st.session_state.role      = ""


def is_logged_in() -> bool:
    init_session()
    return st.session_state.get("logged_in", False)


def is_admin() -> bool:
    return is_logged_in() and st.session_state.get("role") == "Admin"


def require_login():
    """
    Call at the top of any page that needs authentication.
    Stops page execution and shows the login form if not authenticated.
    """
    init_session()
    if not st.session_state.logged_in:
        st.warning("🔒 Please log in from the **Home** page to access this section.")
        st.stop()


def require_admin():
    """
    Call at the top of any page that requires Admin role.
    """
    require_login()
    if st.session_state.role != "Admin":
        st.error("🚫 This page is restricted to **Admin** users only.")
        st.stop()


def show_login_form():
    """
    Renders the login form. Returns True if login succeeded this run.
    """
    init_session()

    st.subheader("🔐 Login")
    with st.form("login_form", clear_on_submit=True):
        username = st.text_input("Username", placeholder="admin / viewer / faculty")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login", use_container_width=True)

    if submitted:
        if login(username, password):
            st.success(f"✅ Welcome, **{st.session_state.username}**! Role: `{st.session_state.role}`")
            st.rerun()
        else:
            st.error("❌ Invalid username or password.")
    return False


def show_user_badge():
    """
    Shows a small sidebar badge with the logged-in user and role.
    Also renders a Logout button.
    """
    if is_logged_in():
        role_icon = "👑" if is_admin() else "👁️"
        st.sidebar.markdown("---")
        st.sidebar.markdown(
            f"{role_icon} **{st.session_state.username}** · `{st.session_state.role}`"
        )
        if st.sidebar.button("Logout", use_container_width=True):
            logout()
            st.rerun()
