import streamlit as st
st.title("Grade Calculator")
st.write("Made by yours truly, Arizzy")
f_grades = st.text_input("What are ur individual formative grades (separate by spaces)? ")
s_grades = st.text_input("What are ur individual summative grades (separate by spaces)? ")
g_goal = st.text_input("What is your goal grade? ")
if st.button("Calculate"):
    try:
        f_grades_list = [float(grade) for grade in f_grades.split()]
        s_grades_list = [float(grade) for grade in s_grades.split()]

        st.write("Formative grades: " + str(f_grades_list))
        st.write("Summative grades: " + str(s_grades_list))

        f_avg = sum(f_grades_list) / len(f_grades_list)
        s_avg = sum(s_grades_list) / len(s_grades_list)
        final_grade = (f_avg * 0.4) + (s_avg * 0.6)

        st.write("Formative average: " + str(f_avg))
        st.write("Summative average: " + str(s_avg))
        st.write("Final grade (weighted): " + str(final_grade))

# Pick ONE image/message based on the grade
        if final_grade != g_goal:
            st.warning("You have not hit your goal yet!, Don't worry keep on working hard!")
        if final_grade == g_goal:
            st.sucess("Good Job! You have hit your goal")
        if final_grade < 70:
            st.warning("We need to get that grade up!")
    
        elif final_grade < 75:
            st.warning("You're close — a little more effort!")
   
        else:
            st.success("Good job, You are passing!")
    except ValueError:
        st.error("Please enter valid number only")
