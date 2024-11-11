from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from config import DATABASE_CONFIG

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the MySQL connection
def get_db_connection():
    return mysql.connector.connect(**DATABASE_CONFIG)

# Route for adding student information
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collecting form data
        name = request.form['name']
        age = request.form['age']
        prn = request.form['prn']
        address = request.form['address']
        department = request.form['department']
        academic_year = request.form['academic_year']

        # Open a database connection and insert data
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check that the number of %s matches the number of values in the tuple
        cursor.execute(
            "INSERT INTO students (name, age, prn, address, department, academic_year) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (name, age, prn, address, department, academic_year)
        )
        
        # Commit the transaction and close the connection
        conn.commit()
        cursor.close()
        conn.close()

        flash("Student information added successfully!")
        return redirect(url_for('index'))

    return render_template('index.html')


# Route for viewing student information based on PRN
@app.route('/view_student', methods=['GET', 'POST'])
def view_student():
    student = None
    if request.method == 'POST':
        prn = request.form['prn']
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE prn = %s", (prn,))
        student = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if not student:
            flash("Student not found.")

    return render_template('view_student.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
