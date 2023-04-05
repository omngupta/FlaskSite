from sqlalchemy import create_engine, text

dbConnectionStr = "mysql+pymysql://t5fjynaoxy90iqrzfcuk:pscale_pw_G89OnKWkmmxGWCjZvOP7xQSFYzwLI1ccceEM8nbzilJ@aws.connect.psdb.cloud/flasksiteprac"

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