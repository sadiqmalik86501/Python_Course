import time
from plyer import notification

while True:
    print("Please Sip Some Water")
    notification.notify(title="Please Drink Some Water",message="You Need To Drink Some Water:")
    time.sleep(60*60)
