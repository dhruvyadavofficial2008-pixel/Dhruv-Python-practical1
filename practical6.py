from abc import ABC, abstractmethod

class BMWCar(ABC):
    """Abstract base class for BMW cars with engines"""
    
    def __init__(self, model, engine_code):
        self.model = model
        self.engine_code = engine_code
        self.engine_running = False
    
    @abstractmethod
    def start_engine(self):
        """Each BMW car must implement its engine start"""
        pass
    
    @abstractmethod
    def performance_stats(self):
        """Each BMW car must show its performance"""
        pass
    
    def car_info(self):  # Concrete method shared by all
        print(f"BMW {self.model} powered by {self.engine_code}")
class BMW_M3(BMWCar):
    """M3 with S58 engine"""
    def __init__(self):
        super().__init__("M3 Competition", "S58")
    
    def start_engine(self):
        print("S58 3.0L twin-turbo inline-6 engine ignites!")
        self.engine_running = True
    
    def performance_stats(self):
        print("503 HP | 479 lb-ft | 0-60 mph in 3.4 seconds")

class BMW_M5(BMWCar):
    """M5 with S63 engine"""
    def __init__(self):
        super().__init__("M5 CS", "S63")
    
    def start_engine(self):
        print("S63 4.4L twin-turbo V8 roars powerfully!")
        self.engine_running = True
    
    def performance_stats(self):
        print("627 HP | 553 lb-ft | 0-60 mph in 2.9 seconds")

class BMW_X5M(BMWCar):
    """X5 M with S63 engine"""
    def __init__(self):
        super().__init__("X5 M Competition", "S63")
    
    def start_engine(self):
        print("S63 4.4L V8 engages with SUV torque!")
        self.engine_running = True
    
    def performance_stats(self):
        print("617 HP | 553 lb-ft | 0-60 mph in 3.7 seconds")

class BMW_540i(BMWCar):
    """540i with B58 engine"""
    def __init__(self):
        super().__init__("540i", "B58")
    
    def start_engine(self):
        print("B58 3.0L turbo inline-6 starts smoothly!")
        self.engine_running = True
    
    def performance_stats(self):
        print("382 HP | 369 lb-ft | 0-60 mph in 4.4 seconds")
# BMW Showroom Demo
cars = [
    BMW_M3(),
    BMW_M5(),
    BMW_X5M(),
    BMW_540i()
]

print("=== BMW CAR & ENGINE SHOWROOM ===\n")

for car in cars:
    print(f"\n--- {car.model} ---")
    car.car_info()
    car.start_engine()
    car.performance_stats()
    print()
