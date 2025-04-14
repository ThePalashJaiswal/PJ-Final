import streamlit as st
from state_info import state_info  # Fixed import: previously was state_info_complete
from offline_centres import offline_centres
from student_categories import student_categories
from student_concerns import student_concerns

st.set_page_config(page_title="Student Assistant App", layout="wide")

st.title("📚 Student Assistant Dashboard")

tabs = st.tabs(["📍 State Judiciary Info", "🏫 Offline Centres", "👥 Student Categories", "🎯 Student Concerns"])

# State Judiciary Info
with tabs[0]:
    st.header("📍 State Judiciary Information")
    state = st.selectbox("Select a state", list(state_info.keys()))
    if state:
        for section, points in state_info[state].items():
            st.subheader(section)
            for point in points:
                st.markdown(f"- {point}")

# Offline Centres
with tabs[1]:
    st.header("🏫 Offline Centre Details")
    centre = st.selectbox("Select an offline centre", list(offline_centres.keys()))
    if centre:
        for section, details in offline_centres[centre].items():
            st.subheader(section)
            for item in details:
                st.markdown(f"- {item}")

# Student Categories
with tabs[2]:
    st.header("👥 Student Category Advisory")
    category = st.selectbox("Select a student category", list(student_categories.keys()))
    if category:
        for section, items in student_categories[category].items():
            st.subheader(section)
            for item in items:
                st.markdown(f"- {item}")

# Student Concerns
with tabs[3]:
    st.header("🎯 Handling Student Concerns")
    concern = st.selectbox("Select a student concern", list(student_concerns.keys()))
    if concern:
        for section, responses in student_concerns[concern].items():
            st.subheader(section)
            for line in responses:
                st.markdown(f"- {line}")
