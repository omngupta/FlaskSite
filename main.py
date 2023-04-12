from flask import Flask, render_template, jsonify, request
from Database import loadJobsFromDB, loadJobFromDB

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

@app.route("/job/<id>")
def show_job(id):
    job = loadJobFromDB(id)
    if not job:
        return 'Not Found', 404
    return render_template('jobDetail.html',job=job, company_name='Kanpuriya')

@app.route("/job/<id>/apply", methods=['post'])
def apply_for_job(id):
    data = request.form
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)