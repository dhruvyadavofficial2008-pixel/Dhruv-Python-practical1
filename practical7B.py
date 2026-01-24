import threading
class Dhruv_Thread(threading.Thread):
    def run(self):
        print("Dhruv Yadav your Thread is runnig")

t = Dhruv_Thread()
t.start()
t.join()
