import threading 
import time 
lock1= threading.Lock() 
lock2= threading.Lock() 
def task1():
    with lock1:
        print("Task 1 acquired lock1")
        time.sleep(1)
        if lock2.acquire(timeout=2):
        else:
            print("Task 1 acquired lock2") lock2.release()
            print("Task 1 could not acquire lock2") 
 
def task2():
    with lock2:
        print("Task 2 acquired lock2")
        time.sleep(1)
        if lock1.acquire (timeout=2):
        else:
            print("Task 2 acquired lock1") lock1.release()
            print("Task 2 could not acquire lock1") 
t1 = threading.Thread (target=task1) 
t2 = threading. Thread (target=task2) 
t1.start() 
t2.start() 
t1.join() 
t2.join() 
print("Execution completed") 
