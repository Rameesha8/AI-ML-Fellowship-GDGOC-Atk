import streamlit as st
from student import Student
from storage import load_students, save_students

st.set_page_config(page_title="Student Management App")

st.title("🎓 Student Management System")

students = load_students()

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Student", "View Students"]
)

if menu == "Add Student":
    st.subheader("Add New Student")

    sid = st.text_input("Student ID")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, step=1)
    grade = st.text_input("Grade")

    if st.button("Add"):
        if not sid or not name:
            st.error("Student ID and Name are required")
        else:
            student = Student(sid, name, age, grade)
            students.append(student.to_dict())
            save_students(students)
            st.success("Student added successfully")

elif menu == "View Students":
    st.subheader("Student Records")

    if students:
        st.table(students)
    else:
        st.info("No students found")
