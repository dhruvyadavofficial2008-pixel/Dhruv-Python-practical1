import threading
def task():
    for i in range(16):
        print(f"Task running: {i}")

t = threading.Thread(target=task)
t.start()
t.join()
