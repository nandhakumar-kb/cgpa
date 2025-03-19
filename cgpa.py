import streamlit as st

# Apply custom CSS for better styling
st.markdown(
    """
    <style>
    body {
        font-family: "Arial", sans-serif;
        background-color: #FFFFFF;
    }
    .stButton > button {
        background-color: #007BFF;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    .stNumberInput input, .stSelectbox select {
        border-radius: 8px;
        padding: 5px;
        border: 2px solid #007BFF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Grade Mapping
GRADE_POINTS = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5}

def calculate_cgpa(grades, credits):
    """Calculate CGPA based on grades and corresponding credits."""
    total_grade_points = sum(GRADE_POINTS[grade] * credit for grade, credit in zip(grades, credits))
    total_credits = sum(credits)
    return total_grade_points / total_credits if total_credits > 0 else 0

# Streamlit UI
st.markdown("<h1 style='color: #007BFF; text-align: center;'>CGPA Calculator</h1>", unsafe_allow_html=True)

# Get number of subjects
subject_count = st.number_input("Enter the number of subjects:", min_value=1, step=1)

# Input Fields for Each Subject
grades = []
credits = []

for i in range(1, subject_count + 1):
    col1, col2 = st.columns(2)
    with col1:
        grade = st.selectbox(f"Grade for Subject {i}", options=list(GRADE_POINTS.keys()), key=f"grade_{i}")
    with col2:
        credit = st.number_input(f"Credit for Subject {i}", min_value=1, step=1, key=f"credit_{i}")

    grades.append(grade)
    credits.append(credit)

# Calculate CGPA on button click
if st.button("Calculate CGPA"):
    if sum(credits) == 0:
        st.error("Total credits cannot be zero.")
    else:
        cgpa = calculate_cgpa(grades, credits)
        st.success(f"Your GPA is: **{cgpa:.2f}**")
        
