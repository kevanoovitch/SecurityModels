import psutil
import time

# Interval (in seconds) to log resource usage
interval = 5

while True:
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    print(
        f"CPU: {cpu_percent}%, Memory: {memory_info.percent}%, Disk: {disk_usage.percent}%")
    time.sleep(interval)
