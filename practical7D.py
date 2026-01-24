import threading
def print_numbers():
    for i in range(7):
        print(f"Number: {i}")

def print_letters():
    for char in "ABCDEFG":
        print(f"Letter: {char}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("Dhruv Yadav your both threads are finished executioning.")
