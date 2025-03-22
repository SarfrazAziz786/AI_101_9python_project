



import streamlit as st 
import time

st.set_page_config(page_title="BMI Calculator", page_icon="📏👩🙎‍♂️" , layout="centered")

st.title("BMI Calculator")

st.markdown("""
Calculate Body Mass Index BMI. 
provide ** weight and height ** to calculate BMI.
""")

col1, col2 = st.columns(2) 
with col1:
  weight = st.number_input("Weight (kg): " , min_value=1.0, format="%.2f")
with col2:
  height = st.number_input("Height (m): " , min_value=1.0, format="%.2f")

if height > 0 and weight > 0:
  bmi = weight / (height ** 2)  #bmi formula
  st.success(f"Your BMI is: {bmi:.2f}")
  st.markdown(f"{bmi:.2f}", unsafe_allow_html=True)

  if bmi < 18.5:
    st.warning("You are underweight. Consider gaining some weight.")
  elif 18.5 <= bmi < 24.9:
    st.success("Congratulations! You have a healthy weight.")
  elif 25 <= bmi < 29.9:
    st.warning("You are overweight. Consider losing some weight.")
  else:
    st.error("You are obese ⚠️. It's important to manage your weight.")

  # **Obesity** is a serious health condition that can lead to various health problems, including heart disease, stroke, type 2 diabetes, and certain types of cancer.

  #           If you are obese, it's crucial to take steps to manage your weight and improve your health. This may involve a combination of lifestyle changes, such as:

else:
  st.warning("Please enter valid height and weight values.") 

