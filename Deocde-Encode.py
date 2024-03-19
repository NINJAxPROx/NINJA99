import os, sys
os.system("git pull")
try:
    __import__("NINJA").NINJA69()
except Exception as e:
    exit(str(e))