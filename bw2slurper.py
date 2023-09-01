import sqlite3
import json

db_connection = sqlite3.connect('../instance/badweather.sql')

try:
    cursor = db_connection.cursor()
    query = "SELECT text FROM pattern WHERE score >= 75"
    cursor.execute(query)
    rows = cursor.fetchall()
    text_fields = [row[0] for row in rows]
    json_output = {"badweather": text_fields}
    json_string = json.dumps(json_output, indent=4)
    print(json_string)

finally:
    db_connection.close()
