@echo off
echo Setting up the app... please wait

pip install -r requirements.txt

echo Starting the app...
start http://127.0.0.1:5000
python wsgi.py

pause