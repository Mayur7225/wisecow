#!/usr/bin/env python3
# Application Health Checker Script

import requests

# URL of the application to monitor
APP_URL = "https://localhost:4499"   # Wisecow TLS container URL
# Use http://localhost:3000 if not using TLS

def check_app_health():
    try:
        response = requests.get(APP_URL, verify=False, timeout=5)
        if response.status_code == 200:
            print(f"[UP] {APP_URL} is running successfully!")
        else:
            print(f"[DOWN] {APP_URL} returned status code {response.status_code}")
    except Exception as e:
        print(f"[DOWN] {APP_URL} is not reachable. Error: {e}")

if __name__ == "__main__":
    check_app_health()

