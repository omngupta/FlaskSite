from flask import Flask, render_template, jsonify
from Database import loadJobsFromDB

app = Flask(__name__)

@app.route("/")
def print_HW():
    jobs = loadJobsFromDB()
    return render_template('home.html',jobs=jobs                            
                           , company_name='Kanpuriya')

@app.route("/api/jobs")
def list_jobs():
    jobs = loadJobsFromDB()
    return jobs

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)