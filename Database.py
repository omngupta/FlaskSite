from sqlalchemy import create_engine, text

dbConnectionStr = "mysql+pymysql://j9bx4ar0je2smmf6tvhv:pscale_pw_PI0SD2OsuvC5uak3WQin3E3Lv77NXSFi3GS2PJQ7jvz@aws.connect.psdb.cloud/flasksiteprac"

dbEngine = create_engine(dbConnectionStr,
    connect_args={
    "ssl" : {
        "ssl_ca":"/etc/ssl/cert.pem"
    }
    })