from abc import ABC, abstractmethod

class Tank(ABC):
    """Abstract base class for military tanks"""
    
    def __init__(self, model, country):
        self.model = model
        self.country = country
        self.engine_running = False
    
    @abstractmethod
    def start_engine(self):
        """Each tank must implement unique engine startup"""
        pass
    
    @abstractmethod
    def combat_specs(self):
        """Each tank must show its combat capabilities"""
        pass
    
    def tank_info(self):  # Concrete method shared by all
        print(f"{self.country} {self.model}")
class Abrams_Tank(Tank):
    """M1A2 Abrams - USA"""
    def __init__(self):
        super().__init__("M1A2 Abrams SEP v3", "USA")
    
    def start_engine(self):
        print("AGT1500 gas turbine engine spools up to 1500 HP")
        self.engine_running = True
    
    def combat_specs(self):
        print("120mm smoothbore gun | 73 rounds | 68 tons | 42 mph top speed")
        print("Depleted uranium armor | 1500 HP turbine | 42 mph")

class T90_Tank(Tank):
    """T-90M Bhishma - Russia/India"""
    def __init__(self):
        super().__init__("T-90M Bhishma", "Russia/India")
    
    def start_engine(self):
        print("V-92S2 diesel engine ignites - 1130 HP")
        self.engine_running = True
    
    def combat_specs(self):
        print("125mm smoothbore gun | 43 rounds | 48 tons | 38 mph top speed")
        print("Relikt ERA | Shtora-1 countermeasures | 60km/h")

class Leopard_Tank(Tank):
    """Leopard 2A7+ - Germany"""
    def __init__(self):
        super().__init__("Leopard 2A7+", "Germany")
    
    def start_engine(self):
        print("MTU MB 873 Ka-501 diesel roars - 1500 HP")
        self.engine_running = True
    
    def combat_specs(self):
        print("120mm L55 gun | 42 rounds | 67 tons | 43 mph top speed")
        print("Composite + spaced armor | 70km/h | IFIS system")

class Challenger_Tank(Tank):
    """Challenger 2 TES - UK"""
    def __init__(self):
        super().__init__("Challenger 2 TES", "UK")
    
    def start_engine(self):
        print("Perkins CV12-9A diesel engine powers up - 1200 HP")
        self.engine_running = True
    
    def combat_specs(self):
        print("120mm rifled L30A1 gun | 64 rounds | 75 tons | 37 mph top speed")
        print("Dorchester armor | 60km/h | 800mm RHA protection")
# Tank demonstration
tanks = [
    Abrams_Tank(),
    T90_Tank(),
    Leopard_Tank(),
    Challenger_Tank()
]

print("=== MAIN BATTLE TANK DEMONSTRATION ===\n")

for tank in tanks:
    print(f"\n--- {tank.model} ---")
    tank.tank_info()
    tank.start_engine()
    tank.combat_specs()
    print("-" * 50)
