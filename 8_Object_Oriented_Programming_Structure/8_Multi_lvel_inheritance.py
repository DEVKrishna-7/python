# Fintech Domain: Digital Payment Hierarchy
class Payment:
    def __init__(self, amount):
        self.amount = amount
    def log_transaction(self):
        print(f"Transaction of ${self.amount} recorded.")

class OnlinePayment(Payment):
    def connect_to_gateway(self):
        print("Connected to Secure Payment Gateway.")

class UPIPayment(OnlinePayment):
    def process(self, upi_id):
        self.connect_to_gateway()  # From Parent
        print(f"Payment of ${self.amount} sent to {upi_id} via UPI.")
        self.log_transaction()     # From Grandparent

# Usage
upi = UPIPayment(500)
upi.process("user@okaxis")

# Automotive/EV Domain: Autonomous Vehicle Stack
class Vehicle:
    def basic_controls(self):
        print("Steering, Braking, and Acceleration systems active.")

class ElectricVehicle(Vehicle):
    def check_battery(self):
        print("Battery at 85%. Range: 400 miles.")

class AutonomousCar(ElectricVehicle):
    def self_drive(self):
        self.basic_controls() # From Grandparent
        self.check_battery()  # From Parent
        print("AI Sensors active. Navigating to destination...")

# Usage
tesla = AutonomousCar()
tesla.self_drive()

# Healthcare/AI Domain: Medical Diagnostic System
class PatientRecord:
    def __init__(self, name):
        self.name = name
    def get_history(self):
        print(f"Retrieving medical history for {self.name}...")

class BloodReport(PatientRecord):
    def get_blood_data(self):
        print("Blood sugar and Cholesterol levels retrieved.")

class AIDiagnosis(BloodReport):
    def predict_health(self):
        self.get_history()    # From Grandparent
        self.get_blood_data() # From Parent
        print("AI Analysis: Low risk of Diabetes detected based on patterns.")

# Usage
diag = AIDiagnosis("Sarah")
diag.predict_health()
