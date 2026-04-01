import subprocess
import time
import sys
import os

def run():
    print("Starting Viva CAD AI Services (Ubuntu)...")
    
    # Start Backend
    backend_path = os.path.join(os.path.dirname(__file__), "backend")
    # Using python3 for Ubuntu
    backend_cmd = ["./venv/bin/python3", "main.py"]
    print(f"Launching Backend: {backend_cmd}")
    backend_proc = subprocess.Popen(backend_cmd, cwd=backend_path)
    
    # Wait for backend to initialize
    time.sleep(2)
    
    # Start Frontend
    frontend_path = os.path.join(os.path.dirname(__file__), "frontend")
    frontend_cmd = ["npm", "run", "dev"]
    print(f"Launching Frontend: {frontend_cmd}")
    # npm is standard on Ubuntu
    frontend_proc = subprocess.Popen(frontend_cmd, cwd=frontend_path)
    
    try:
        while True:
            time.sleep(1)
            if backend_proc.poll() is not None or frontend_proc.poll() is not None:
                break
    except KeyboardInterrupt:
        print("\nStopping services...")
    finally:
        backend_proc.terminate()
        frontend_proc.terminate()

if __name__ == "__main__":
    run()
