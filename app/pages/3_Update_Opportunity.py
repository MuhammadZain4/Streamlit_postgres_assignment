import streamlit as st
from queries import get_all_opportunities, update_opportunity_status # Adjust imports

st.set_page_config(page_title="Update Opportunity", page_icon="✏️", layout="wide")

if not st.session_state.get("authenticated", False):
    st.warning("Please login from the Home page first.")
elif st.session_state.get("role") != "Admin":
    st.error("⛔ Access Denied! Only Faculty Admins can update data.")
else:
    st.title("✏️ Update Opportunity Status & Info")
    st.markdown("---")

    try:
        df = get_all_opportunities()
        if not df.empty:
            # Let user select opportunity via dropdown
            options = {f"{row['opportunity_id']} - {row['job_title']} at {row['company_name']}": row['opportunity_id'] for _, row in df.iterrows()}
            selected_opt = st.selectbox("Select an Opportunity to Update", list(options.keys()))
            
            opp_id = options[selected_opt]
            current_row = df[df['opportunity_id'] == opp_id].iloc[0]

            with st.form("update_form"):
                st.write(f"Updating ID: `{opp_id}`")
                new_status = st.selectbox("Change Status", ["Open", "Closed", "Expired", "Shortlisted"], index=["Open", "Closed", "Expired", "Shortlisted"].index(current_row['status']))
                new_mode = st.selectbox("Change Work Mode", ["Onsite", "Remote", "Hybrid"], index=["Onsite", "Remote", "Hybrid"].index(current_row['work_mode']))
                
                submitted = st.form_submit_button("Save Changes")
                if submitted:
                    update_opportunity_status(opp_id, new_status, new_mode)
                    st.success("Record updated successfully!")
                    st.rerun()
        else:
            st.info("No records available to update.")
    except Exception as e:
        st.error(f"Error: {e}")