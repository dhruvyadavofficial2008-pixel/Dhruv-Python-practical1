import threading
def greet():
    print("Hello Dhruv Yadav from thread!")

t = threading.Thread(target=greet)
t.start()
t.join()
