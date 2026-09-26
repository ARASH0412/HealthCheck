import psutil
import logging
from datetime import datetime

logging.basicConfig(filename='heath.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

message = f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"
logging.info(message)
print(message)

if cpu > 80:
    logging.warning(f"HIGH CPU USAGE: {cpu}%")
if memory > 80:
    logging.warning(f"HIGH MEMORY USAGE: {memory}%")
if disk > 90:
    logging.warning(f"LOW DISK SPACE: {disk}%")

