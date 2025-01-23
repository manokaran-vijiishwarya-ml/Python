import schedule
import time

def job():
    print("Doing the task...")

schedule.every(10).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(2)