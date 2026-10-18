
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Basic Calculator",
    page_icon="🧮",
    layout="centered"
)

# UI
st.title("🧮 Basic Calculator")
st.write("Perform basic arithmetic operations.")

# Input numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Select operation
operation = st.selectbox(
    "Choose an operation",
    ["Addition (+)", "Subtraction (-)",
     "Multiplication (*)", "Division (/)"]
)

# Calculate result
if st.button("Calculate", type="primary"):
    if operation == "Addition (+)":
        result = num1 + num2

    elif operation == "Subtraction (-)":
        result = num1 - num2

    elif operation == "Multiplication (*)":
        result = num1 * num2

    elif operation == "Division (/)":
        if num2 == 0:
            st.error("Cannot divide by zero!")
            st.stop()
        result = num1 / num2

    st.success(f"Result: {result:g}")
