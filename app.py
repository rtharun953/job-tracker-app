from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

if not os.path.exists("database.db"):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE jobs (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, company TEXT, status TEXT)''')
    conn.commit()
    conn.close()
    
@app.route('/')
def home():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM jobs")
    jobs = c.fetchall()
    conn.close()
    return render_template("index.html", jobs=jobs)

@app.route('/')
def add_job():
    title = request.form.get("title")
    company = request.form.get("company")
    status = request.form.get("status")

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO jobs (title, company, status) VALUES (?, ?, ?)",(title, company,status))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)