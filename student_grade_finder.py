# Python Streamlit app to find the grade of a student
# Get the mark from the student
# Determine the grade based on the mark
# Present a motivational message based on the grade with some background effects

import streamlit as st
import datetime

st.title("Student Grade Finder")

if "show_grade" not in st.session_state:
    st.session_state.show_grade = False
if "grade" not in st.session_state:
    st.session_state.grade = ""

with st.form("grade_form"):
    # Get the mark from the student
    mark = st.number_input("Enter your mark:", min_value=0, max_value=100)
    submitted = st.form_submit_button("Get Grade")

    if submitted:
        # Determine the grade only when the form is submitted
        if mark >= 90 and mark <= 100:
            st.session_state.grade = "A"
        elif mark >= 80 and mark < 90:
            st.session_state.grade = "B"
        elif mark >= 70 and mark < 80:
            st.session_state.grade = "C"
        elif mark >= 60 and mark < 70:
            st.session_state.grade = "D"
        else:
            st.session_state.grade = "E"

        st.session_state.show_grade = True

if st.session_state.show_grade:
    grade = st.session_state.grade

    # Present a motivational message based on the grade with some background effects
    st.subheader(f"Grade: {grade}")

    if grade == "A":
        st.success("Excellent work! Keep up the great work!")
        st.balloons()
    elif grade == "B":
        st.info("Good job! You're doing well!")
        st.snow()
    elif grade == "C":
        st.warning("You're doing okay, but there's room for improvement.")
    elif grade == "D":
        st.error("You need to put in more effort.")
    else:
        st.error("You need to study harder.")

    # Display the current date and time
    st.write(f"Current date and time: {datetime.datetime.now()}")