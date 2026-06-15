from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()


class WellnessEntry(BaseModel):
    employee_name: str
    mood: str
    stress_level: int
    energy_level: int
    notes: str


@app.get("/")
def home():
    return {
        "message": "Smart Wellness Tracker API"
    }


@app.get("/entries")
def get_entries():

    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="8464",
        database="wellness_tracker"
    )

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM wellness_entries
        ORDER BY created_at DESC
    """)

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records


@app.post("/add-entry")
def add_entry(entry: WellnessEntry):

    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="8464",
        database="wellness_tracker"
    )

    cursor = connection.cursor()

    query = """
        INSERT INTO wellness_entries
        (
            employee_name,
            mood,
            stress_level,
            energy_level,
            notes
        )
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        entry.employee_name,
        entry.mood,
        entry.stress_level,
        entry.energy_level,
        entry.notes
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "message": "Entry added successfully"
    }