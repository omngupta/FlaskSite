from flask import Flask, render_template, jsonify
from Database import dbEngine
from sqlalchemy import text

app = Flask(__name__)

def loadJobsFromDB():
    with dbEngine.connect() as conn:
        result = conn.execute(text('select * from jobs'))
        jobs = []
        for row in result.all():
            jobs.append(row)
        return jobs    

@app.route("/")
def print_HW():
    jobs = loadJobsFromDB()
    return render_template('home.html',jobs=jobs                            
                           , company_name='Kanpuriya')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)