import psutil
import time
while True:
    cpu_usage=psutil.cpu_percent(interval=1)
    print(time.asctime())
    print(f"CPU Usage: {cpu_usage}%")
    mem = psutil.virtual_memory().percent
    print(f"memory used :{mem}")
    print("")
    time.sleep(5)
