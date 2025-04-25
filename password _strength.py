import streamlit as st
import re

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak", "red"
    elif score == 3 or score == 4:
        return "Moderate", "orange"
    else:
        return "Strong", "green"

st.title("Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    strength, color = check_strength(password)
    st.markdown(f"**Strength:** <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)
