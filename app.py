import streamlit as st
import pandas as pd

st.title("🚆 Coach Health Monitoring System")

# ✅ CSV LOAD (ye line missing hai tumhare code me)
data = pd.read_csv("coach_data.csv")

# Function
def check_health(temp, vib, door):
    if temp > 40 or vib > 1.0 or door == "Open":
        return "Maintenance Required"
    else:
        return "Healthy"

# Apply logic
data["Status"] = data.apply(lambda row: check_health(
    row["Temperature"], row["Vibration"], row["Door_Status"]), axis=1)

# Show data
st.subheader("📊 Coach Data")
st.dataframe(data)

# Divider
st.markdown("---")

# Input section
st.subheader("🔍 Check New Coach")

temp = st.slider("Temperature", 0, 100, 30)
vib = st.slider("Vibration", 0.0, 2.0, 0.5)
door = st.selectbox("Door Status", ["Closed", "Open"])

if st.button("Check Status"):
    result = check_health(temp, vib, door)

    if result == "Healthy":
        st.success("✅ Coach is Healthy")
    else:
        st.error("⚠️ Maintenance Required")