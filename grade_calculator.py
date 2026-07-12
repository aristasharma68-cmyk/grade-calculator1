import streamlit as st
if "page" not in st.session_state:
    st.session_state.page = "grade"

if st.button("Compound Interest Calculator"):
    st.session_state.page = "compound"

if st.button("Back to Grade Calculator"):
    st.session_state.page = "grade"
    if st.session_state.page = "grade":
    st.title("Grade Calculator")
    st.write("Made by yours truly, Arizzy")
    f_grades = st.text_input("What are ur individual formative grades (separate by spaces)? ")
    s_grades = st.text_input("What are ur individual summative grades (separate by spaces)? ")
    g_goal = st.text_input("What is your goal grade? ")
    col1, col2, col3 = st.columns(3)
    with col1:
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
                st.success("Final grade (weighted): " + str(final_grade))
       
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
                
                rounded_grade = round(final_grade)
                if rounded_grade == 67:
                    st.audio("67 bloxfruit.mp3", autoplay = True)
                elif rounded_grade == 21:
                    st.audio("21 meme.mp3", autoplay = True)
                elif rounded_grade == 100:
                    st.audio("mewing.mp3", autoplay = True)
                if rounded_grade == 69:
                    st.audio("sus.mp3", autoplay = True)
        except ValueError:
            st.error("Please enter valid number only")
with col2:
    if st.button("Restart"):
        st.rerun()
with col3:
        if st.button("Compound Interest Calculator"):
            st.session_state.page = "compound"


elif st.session_state.page == "compound":
    st.title("Compound Interest Calculator")
    if st.button("Back to grade calculator"):
        st.session_state.page = "grade"
    
    princi = st.text_input("Type in your principal.")
    annual = st.text_input("Type in your annual interest as a decimal. (divide your percentage by 100)")
    howmany = st.text_input("Type in how many times per year it compounds")
    times = st.text_input("Type in number of years.")
    
    if st.button("Calculate Compound Interest"):
        try:
            princi = float(princi)
            annual = float(annual)
            howmany = int(howmany)
            times = int(times)

            step2 = annual / howmany
            step3 = howmany * times
            step4 = (1 + step2) ** step3
            step5 = step4 * princi
            step6 = step5 - princi

            st.write("Rate per period: " + str(step2))
            st.write("Total compounding periods: " + str(step3))
            st.write("Growth multiplier: " + str(step4))
            st.success("Final amount: " + str(step5))
            st.write("Interest earned: " + str(step6))
        except ValueError:
            st.error("Please enter valid numbers only.")
