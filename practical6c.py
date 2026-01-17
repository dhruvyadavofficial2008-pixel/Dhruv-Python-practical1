from abc import ABC, abstractmethod

# Interface 1: All warships must be able to fire
class Fireable(ABC):
    """Interface for warships that can fire weapons"""
    
    @abstractmethod
    def fire_main_guns(self):
        pass
    
    @abstractmethod
    def missile_launch(self):
        pass

# Interface 2: All warships must have propulsion
class Propulsible(ABC):
    """Interface for warships propulsion systems"""
    
    @abstractmethod
    def engage_engines(self):
        pass
    
    @abstractmethod
    def max_speed(self):
        pass
class Iowa_Battleship(Fireable, Propulsible):
    """WWII Iowa-class Battleship"""
    def __init__(self):
        self.name = "USS Iowa (BB-61)"
        self.displacement = "58,000 tons"
    
    def fire_main_guns(self):
        print("16-inch/50 cal guns fire - 2,700 lb shells at 30,000 yards!")
    
    def missile_launch(self):
        print("Tomahawk missiles launched from VLS cells")
    
    def engage_engines(self):
        print("4x General Electric turbines - 212,000 shaft HP")
    
    def max_speed(self):
        print("33 knots | 38 mph | 2,500 nautical miles range")

class Arleigh_Burke_Destroyer(Fireable, Propulsible):
    """Modern Aegis Destroyer"""
    def __init__(self):
        self.name = "USS Arleigh Burke (DDG-51)"
        self.displacement = "9,200 tons"
    
    def fire_main_guns(self):
        print("5-inch/62 cal Mk45 gun rapid fire - 20+ miles range")
    
    def missile_launch(self):
        print("96 VLS cells: SM-6, Tomahawk, ASROC missiles")
    
    def engage_engines(self):
        print("4x GE LM2500 gas turbines - 100,000 shaft HP")
    
    def max_speed(self):
        print("30+ knots | 35+ mph | Stealth design")

class Nimitz_Carrier(Fireable, Propulsible):
    """Nuclear Aircraft Carrier"""
    def __init__(self):
        self.name = "USS Nimitz (CVN-68)"
        self.displacement = "100,000 tons"
    
    def fire_main_guns(self):
        print("Sea Sparrow missiles & Phalanx CIWS defensive fire")
    
    def missile_launch(self):
        print("Aircraft deliver precision strikes - 75+ planes")
    
    def engage_engines(self):
        print("2x A4W nuclear reactors - Unlimited range")
    
    def max_speed(self):
        print("30+ knots | 35+ mph | 20+ years without refueling")

class Type_055_Destroyer(Fireable, Propulsible):
    """Chinese Renhai-class Destroyer"""
    def __init__(self):
        self.name = "Type 055 Renhai"
        self.displacement = "13,000 tons"
    
    def fire_main_guns(self):
        print("130mm H/PJ-38 gun - 100+ km guided shells")
    
    def missile_launch(self):
        print("112 VLS cells: YJ-18 anti-ship, HQ-9 SAMs")
    
    def engage_engines(self):
        print("Combined gas and gas - 110,000 shaft HP")
    
    def max_speed(self):
        print("30 knots | 35 mph | Stealth hull design")
# Warship fleet
warships = [
    Iowa_Battleship(),
    Arleigh_Burke_Destroyer(),
    Nimitz_Carrier(),
    Type_055_Destroyer()
]

print("=== NAVAL WARSHIP FLEET INTERFACE DEMO ===\n")

for ship in warships:
    print(f"\n--- {ship.name} ---")
    print(f"Displacement: {ship.displacement}")
    ship.fire_main_guns()
    ship.missile_launch()
    ship.engage_engines()
    ship.max_speed()
    print("-" * 60)
