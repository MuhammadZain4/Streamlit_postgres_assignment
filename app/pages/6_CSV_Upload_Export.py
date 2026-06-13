import streamlit as st
import pandas as pd
from queries import insert_opportunity, get_all_opportunities # Adjust imports

st.set_page_config(page_title="CSV Upload & Export", page_icon="📂", layout="wide")

if not st.session_state.get("authenticated", False):
    st.warning("Please login from the Home page first.")
else:
    st.title("📂 Bulk CSV Operations")
    
    tab1, tab2 = st.tabs(["📥 Bulk Import via CSV", "📤 Export Filtered Data"])
    
    with tab1:
        st.header("Upload CSV Data File")
        if st.session_state.get("role") != "Admin":
            st.error("Only Admins can perform bulk data inserts.")
        else:
            uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
            if uploaded_file is not None:
                try:
                    df_upload = pd.read_csv(uploaded_file)
                    st.write("Preview of Uploaded Data:")
                    st.dataframe(df_upload.head(), use_container_width=True)
                    
                    # Simple validation checkpoint
                    required_cols = ['company_name', 'job_title', 'category', 'work_mode', 'required_skills']
                    if all(col in df_upload.columns for col in required_cols):
                        if st.button("Insert Valid Rows into Database"):
                            success_count = 0
                            for _, row in df_upload.iterrows():
                                try:
                                    insert_opportunity(
                                        row['company_name'], row['job_title'], row['category'],
                                        row.get('city', 'Lahore'), row.get('country', 'Pakistan'),
                                        row['work_mode'], row['required_skills'],
                                        float(row.get('salary_min', 0)), float(row.get('salary_max', 0)),
                                        row.get('currency', 'PKR'), pd.to_datetime(row.get('application_deadline')).date()
                                    )
                                    success_count += 1
                                except Exception:
                                    continue
                            st.success(f"🎉 Successfully imported {success_count} opportunities into PostgreSQL!")
                    else:
                        st.error(f"CSV must contain mandatory columns: {required_cols}")
                except Exception as e:
                    st.error(f"Error parsing CSV file: {e}")
                    
    with tab2:
        st.header("Export Records to CSV")
        try:
            df_export = get_all_opportunities()
            if not df_export.empty:
                st.write(f"Total available rows for backup: `{len(df_export)}`")
                csv_data = df_export.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Data Spreadsheet as CSV",
                    data=csv_data,
                    file_name='exported_opportunities_data.csv',
                    mime='text/csv'
                )
            else:
                st.info("No records available to export.")
        except Exception as e:
            st.error(f"Export Error: {e}")