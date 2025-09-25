#!/usr/bin/env python3
# System Health Monitoring Script

import psutil
import datetime

# Thresholds
CPU_THRESHOLD = 80      # percent
MEM_THRESHOLD = 70      # percent
DISK_THRESHOLD = 80     # percent

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    alerts = []

    if cpu > CPU_THRESHOLD:
        alerts.append(f"[ALERT] CPU usage high: {cpu}%")
    if mem > MEM_THRESHOLD:
        alerts.append(f"[ALERT] Memory usage high: {mem}%")
    if disk > DISK_THRESHOLD:
        alerts.append(f"[ALERT] Disk usage high: {disk}%")

    if alerts:
        print(f"\nSystem Health Alerts - {datetime.datetime.now()}")
        for alert in alerts:
            print(alert)
    else:
        print(f"System OK - CPU: {cpu}%, Memory: {mem}%, Disk: {disk}%")

if __name__ == "__main__":
    check_system_health()

