# app/utils.py
import streamlit as st

def format_currency(amount, currency="PKR"):
    """
    Salary amount ko proper thousand separators ke sath format karne ke liye.
    Example: 150000 -> 150,000 PKR
    """
    try:
        if amount is None:
            return "N/A"
        return f"{int(amount):,} {currency}"
    except (ValueError, TypeError):
        return "N/A"

def format_salary_range(min_sal, max_sal, currency="PKR"):
    """
    Minimum aur Maximum salary ko combine karke dashboard/views ke liye range banana.
    """
    if min_sal == 0 and max_sal == 0:
        return "Not Specified / Competitive"
    return f"{format_currency(min_sal, currency)} - {format_currency(max_sal, currency)}"

def get_status_color(status):
    """
    Status ke mutabiq dashboard ya lists ke liye custom Bootstrap/HTML color alerts return karna.
    """
    status_lower = str(status).lower()
    if status_lower == 'open':
        return "green"
    elif status_lower == 'closed':
        return "red"
    elif status_lower == 'filled':
        return "blue"
    return "grey"

def local_css(file_name):
    """
    Agar Streamlit UI mein custom alignment ya design tweaks inject karne hon.
    """
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        pass