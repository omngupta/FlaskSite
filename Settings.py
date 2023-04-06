
import os

def setEnvironmentVaribales():
    with open('.env','r') as envFile:
        lines=envFile.readlines()
        for ln in lines:
            os.environ[ln[0:ln.find('=')]] = ln[ln.find('=')+1:]