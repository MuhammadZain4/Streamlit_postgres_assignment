import streamlit as st
from queries import get_all_opportunities, delete_opportunity  # Adjust import based on queries.py

st.set_page_config(page_title="Delete Opportunity", page_icon="🗑️", layout="wide")

if not st.session_state.get("authenticated", False):
    st.warning("Please login from the Home page first.")
elif st.session_state.get("role") != "Admin":
    st.error("⛔ Access Denied! Only Faculty Admins can delete data from the database.")
else:
    st.title("🗑️ Delete Opportunity")
    st.markdown("---")

    try:
        df = get_all_opportunities()
        if not df.empty:
            # Let user select record to delete
            options = {f"{row['opportunity_id']} - {row['job_title']} at {row['company_name']}": row['opportunity_id'] for _, row in df.iterrows()}
            selected_opt = st.selectbox("Select a Record to Permanently Remove", list(options.keys()))
            
            opp_id = options[selected_opt]
            current_row = df[df['opportunity_id'] == opp_id].iloc[0]

            # Preview before delete
            st.warning(f"⚠️ You are about to delete: **{current_row['job_title']}** at **{current_row['company_name']}**")
            st.write(f"**City:** {current_row['city']} | **Category:** {current_row['category']}")
            
            confirm = st.checkbox("I confirm that I want to delete this record permanently.")
            
            if st.button("Delete Record", type="primary"):
                if confirm:
                    delete_opportunity(opp_id)
                    st.success("🔥 Record deleted successfully from PostgreSQL!")
                    st.rerun()
                else:
                    st.error("Please check the confirmation box first.")
        else:
            st.info("No records available to delete.")
    except Exception as e:
        st.error(f"Error: {e}")