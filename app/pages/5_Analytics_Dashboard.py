import streamlit as st
import plotly.express as px
from queries import get_all_opportunities  # Adjust based on queries.py

st.set_page_config(page_title="Analytics Dashboard", page_icon="📊", layout="wide")

if not st.session_state.get("authenticated", False):
    st.warning("Please login from the Home page first.")
else:
    st.title("📊 Internship & Job Analytics Dashboard")
    st.markdown("---")

    try:
        df = get_all_opportunities()
        if not df.empty:
            # --- 6 KPIs ---
            st.subheader("📌 Key Performance Indicators (KPIs)")
            kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)
            
            kpi1.metric("Total Jobs", len(df))
            kpi2.metric("Open Status", len(df[df['status'] == 'Open']))
            kpi3.metric("Closed Status", len(df[df['status'] == 'Closed']))
            kpi4.metric("Remote Roles", len(df[df['work_mode'] == 'Remote']))
            kpi5.metric("Unique Companies", df['company_name'].nunique())
            kpi6.metric("Avg Min Salary (PKR)", f"{df[df['currency']=='PKR']['salary_min'].mean():,.0f}")

            st.markdown("---")
            st.subheader("📈 Visual Trends & Distributions")

            col1, col2 = st.columns(2)
            
            with col1:
                # Chart 1: Jobs by Category
                fig1 = px.bar(df, x='category', title="Jobs Count by Category", color='category')
                st.plotly_chart(fig1, use_container_width=True)
                
                # Chart 2: Work Mode Breakdown
                fig2 = px.pie(df, names='work_mode', title="Work Mode Breakdown", hole=0.3)
                st.plotly_chart(fig2, use_container_width=True)

            with col2:
                # Chart 3: Jobs by City
                fig3 = px.histogram(df, x='city', title="Geographical Distribution (Cities)", color='city')
                st.plotly_chart(fig3, use_container_width=True)
                
                # Chart 4: Salary Range Box Plot
                fig4 = px.box(df, x='category', y='salary_max', title="Salary Max Distribution by Category", color='category')
                st.plotly_chart(fig4, use_container_width=True)

            # Chart 5: Status Breakdown across Categories
            fig5 = px.bar(df, x='category', color='status', title="Opportunity Status Matrix by Domain", barmode='group')
            st.plotly_chart(fig5, use_container_width=True)

        else:
            st.info("No data available to plot charts.")
    except Exception as e:
        st.error(f"Analytics Error: {e}")