from sqlalchemy import create_engine, text
from Settings import setEnvironmentVaribales
import os

# Set & Get Env Variables
setEnvironmentVaribales()
dbUser = os.environ['DBUSER'].strip()
dbPwd = os.environ['DBPWD'].strip()
dbHost = os.environ['DBHOST'].strip()
dbName = os.environ['DBNAME'].strip()

dbConnectionStr = f"mysql+pymysql://{dbUser}:{dbPwd}@{dbHost}/{dbName}"

dbEngine = create_engine(dbConnectionStr,
    connect_args={
    "ssl" : {
        "ssl_ca":"/etc/ssl/cert.pem"
    }
    })

def loadJobsFromDB():
    with dbEngine.connect() as conn:
        result = conn.execute(text('select * from jobs'))
        jobs = []
        for row in result.all():
            jobs.append(row)
        return jobs
    
def loadJobFromDB(id):
    with dbEngine.connect() as conn:
        result = conn.execute(text(f"select * from jobs where id ={id}"))
        rows=result.all()

        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()
        
def addApplicationToDB(job_id, data):
  with dbEngine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    # conn.execute(query, job_id=job_id, full_name=data['full_name'], email=data['email'], linkedin_url=data['linkedin_url'], education=data['education'], work_experience=data['work_experience'], resume_url=data['resume_url'])
    conn.execute(query, {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'work_experience': data['work_experience'],
            'resume_url': data['resume_url']
        })
        


  