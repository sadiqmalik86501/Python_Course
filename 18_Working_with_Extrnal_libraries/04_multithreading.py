import threading
import time

def worker(num):
    print(f"Threading {num} Starting:")
    time.sleep(2)
    print(f"Thread {num}:finishing")


threads=[]
for i in range(3):
    thread=threading.Thread(target=worker,args=(i,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print("All Threads Completed!")