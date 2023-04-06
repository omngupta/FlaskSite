
import os

def setEnvironmentVaribales():
    try:    
        with open('.env','r') as envFile:
            lines=envFile.readlines()
            for ln in lines:
                os.environ[ln[0:ln.find('=')]] = ln[ln.find('=')+1:]
    except: 
        print("Something went wrong when opening the file or Production mode.")