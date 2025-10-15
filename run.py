import os
import time
import sys

python_executable = sys.executable

backend_command = f'start "Backend Server" cmd /k "{python_executable}" -m uvicorn api.main:app'

frontend_command = f'start "Frontend UI" cmd /k "{python_executable}" -m streamlit run app.py'

print("--- Opening backend server in a new window... ---")
os.system(backend_command)

time.sleep(5)

print("--- Opening frontend UI in a new window... ---")
os.system(frontend_command)

print("\n🚀 Your application servers are starting in new terminal windows.")
print("Please check the new windows for the server status and URLs.")