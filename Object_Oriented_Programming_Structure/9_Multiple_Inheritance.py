# 1. GRANDPARENT CLASS: Basic Package Info
class Package:
    def __init__(self, weight):
        self.weight = weight

    def calculate_base_cost(self):
        cost = self.weight * 2  # $2 per kg
        print(f"Base Shipping Cost: ${cost}")
        return cost

# 2. PARENT CLASS: Adds Tracking (Inherits from Package)
class TrackablePackage(Package):
    def get_tracking_status(self):
        print("Status: Package is at the local sorting facility.")

# 3. CHILD CLASS: Adds Express Delivery (Inherits from TrackablePackage)
class ExpressPackage(TrackablePackage):
    def __init__(self, weight, priority_level):
        # Using the grandparent's constructor
        super().__init__(weight)
        self.priority = priority_level

    def deliver_now(self):
        # Accessing Grandparent's method
        self.calculate_base_cost()
        # Accessing Parent's method
        self.get_tracking_status()
        print(f"Action: Delivering with {self.priority} priority via Air Freight!")

# --- Execution ---
# Creating the most specialized object
my_order = ExpressPackage(weight=5, priority_level="High")

# The Child object can access everything in the chain:
my_order.deliver_now()
