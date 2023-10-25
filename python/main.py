import mysql.connector
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def index():
    connection = mysql.connector.connect(
        user="root", password="root",host='mysql', port = 3306, database= 'db')
    print("DB Connected")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    stud_details = cursor.fetchall()
    connection.close()

    print(stud_details)
    return jsonify(stud_details)

if __name__ == "__main__":
    app.run(host='0.0.0.0')