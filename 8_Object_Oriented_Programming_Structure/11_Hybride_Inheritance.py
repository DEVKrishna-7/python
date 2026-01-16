class A:
    def method1(self):
        print("a")
class B(A):
    def method2(self):
        print("b")
class C(A):
    def method3(self):
        print("c")
class D(B,C):
    def method4(self):
        print("d")

obj=D()
obj.method4() # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B

# 1. Base Class (The Root)
class Device:
    def __init__(self, brand):
        self.brand = brand
    def power_info(self):
        print(f"Device Brand: {self.brand}")

# 2. Hierarchical Level (Two children from one parent)
class Electronic(Device):
    def voltage_check(self):
        print("Voltage is stable at 220V.")

class WiFiEnabled(Device):
    def connect_internet(self):
        print("Connected to 6G Home Network.")

# 3. Multiple Inheritance Level (One child from two parents)
# This creates the HYBRID structure
class SmartCamera(Electronic, WiFiEnabled):
    def start_recording(self):
        self.power_info()       # From Grandparent (Device)
        self.voltage_check()    # From Parent 1 (Electronic)
        self.connect_internet() # From Parent 2 (WiFiEnabled)
        print("Camera: Recording high-def footage to cloud...")

# --- Execution ---
my_cam = SmartCamera("Sony-AI")
my_cam.start_recording()
