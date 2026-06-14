import streamlit as st
import mysql.connector
import pandas as pd

# Database Connection
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="8464",
    database="wellness_tracker"
)

cursor = connection.cursor()

st.title("Smart Wellness Tracker")

# Form
name = st.text_input("Employee Name")

mood = st.selectbox(
    "Mood",
    ["Happy", "Neutral", "Sad", "Stressed"]
)

stress = st.number_input(
    "Stress Level",
    min_value=1,
    max_value=10
)

energy = st.number_input(
    "Energy Level",
    min_value=1,
    max_value=10
)

notes = st.text_area("Notes")

# Submit Button
if st.button("Save Entry"):

    if not name.strip():
        st.error("Employee Name is required")

    else:
        query = """
        INSERT INTO wellness_entries
        (employee_name, mood, stress_level, energy_level, notes)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            name,
            mood,
            stress,
            energy,
            notes
        )

        cursor.execute(query, values)
        connection.commit()

        st.success("Entry Saved Successfully!")

# =========================
# DASHBOARD METRICS
# =========================

cursor.execute("""
SELECT
    COUNT(*),
    AVG(stress_level),
    AVG(energy_level)
FROM wellness_entries
""")

result = cursor.fetchone()

total_entries = result[0]
avg_stress = result[1]
avg_energy = result[2]

st.subheader("Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Entries",
    total_entries
)

col2.metric(
    "Average Stress",
    float(round(avg_stress, 2)) if avg_stress else 0
)

col3.metric(
    "Average Energy",
    float(round(avg_energy, 2)) if avg_energy else 0
)

# =========================
# MOOD DISTRIBUTION CHART
# =========================

cursor.execute("""
SELECT mood, COUNT(*)
FROM wellness_entries
GROUP BY mood
""")

mood_data = cursor.fetchall()

if mood_data:

    mood_df = pd.DataFrame(
        mood_data,
        columns=["Mood", "Count"]
    )

    st.subheader("Mood Distribution")

    st.bar_chart(
        mood_df.set_index("Mood")
    )

# =========================
# WELLNESS HISTORY TABLE
# =========================

st.subheader("Wellness History")

cursor.execute("""
SELECT *
FROM wellness_entries
ORDER BY created_at DESC
""")

rows = cursor.fetchall()

columns = [
    "ID",
    "Employee Name",
    "Mood",
    "Stress Level",
    "Energy Level",
    "Notes",
    "Created At"
]

df = pd.DataFrame(
    rows,
    columns=columns
)

st.dataframe(
    df,
    use_container_width=True
)