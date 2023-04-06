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