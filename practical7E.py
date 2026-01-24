import threading 
counter = 0 
lock = threading.Lock()
def increment():
    global counter
    for i in range(46216):
        with lock:
            counter += 1 

t1 = threading. Thread (target=increment) 
t2 = threading.Thread (target=increment) 

t1.start() 
t2.start() 
 
t1.join() 
t2.join() 
print("Final counter value:", counter) 
print("Dhruv Yadav F126")
