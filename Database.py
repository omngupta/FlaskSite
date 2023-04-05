from sqlalchemy import create_engine, text

dbConnectionStr = "mysql+pymysql://au2fc3i18fscjloyka9f:pscale_pw_QA8iZyPTfzwAwipE69OoIEZK4jZFh7pIPSflTCF9PC@aws.connect.psdb.cloud/flasksiteprac"

dbEngine = create_engine(dbConnectionStr,
    connect_args={
    "ssl" : {
        "ssl_ca":"/etc/ssl/cert.pem"
    }
    })