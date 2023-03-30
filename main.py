from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Gurgaon, India',
        'salary':'Rs 12,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Bangalore, India',
        'salary':'Rs 15,00,000'
    },
    {
        'id':3,
        'title':'Xamarin Developer',
        'location':'London, UK',
        'salary':'£75,000'
    }
]

@app.route("/")
def print_HW():
    return render_template('home.html',jobs=JOBS                            
                           , company_name='Ban De Fukrey')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)