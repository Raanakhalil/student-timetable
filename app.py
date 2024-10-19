import streamlit as st
import pandas as pd

# App title
st.title("Student Day Timetable Planner")

# Introduction
st.write("Create your timetable for the day by entering the subjects and their respective times.")

# Create an empty DataFrame to store the timetable
if 'timetable' not in st.session_state:
    st.session_state.timetable = pd.DataFrame(columns=["Subject", "Start Time", "End Time"])

# User input for subjects and times
with st.form(key='timetable_form'):
    subject = st.text_input("Enter the subject")
    start_time = st.time_input("Enter start time", key="start_time")
    end_time = st.time_input("Enter end time", key="end_time")

    submit_button = st.form_submit_button("Add to Timetable")

    if submit_button and subject:
        new_row = {"Subject": subject, "Start Time": start_time, "End Time": end_time}
        st.session_state.timetable = st.session_state.timetable.append(new_row, ignore_index=True)
        st.success(f"Added {subject} to timetable!")

# Display the timetable
if not st.session_state.timetable.empty:
    st.write("### Your Day's Timetable:")
    st.table(st.session_state.timetable)

# Option to clear the timetable
if st.button("Clear Timetable"):
    st.session_state.timetable = pd.DataFrame(columns=["Subject", "Start Time", "End Time"])
    st.success("Timetable cleared!")
