from datetime import datetime
import time

class Machine:
    def __init__(self,cloud_service, machine_type,cost_per_minute):
        self.machine_type = machine_type
        self.cost_per_minute = cost_per_minute
        self.start_time = None
        self.end_time = None
        self.total_cost = 0
        cloud_service.add_machine(self)

    def start_machine(self):
        if self.start_time is not None:
            print("Machine is already running.")
            return
        self.start_time = datetime.now()

    def stop_machine(self):
        if self.start_time is None:
            print("Machine is not running.")
            return
        self.end_time = datetime.now()
        delta_minutes = (self.end_time - self.start_time).total_seconds() / 60
        self.total_cost += delta_minutes * self.cost_per_minute
        self.start_time = None


class CloudService:
    def __init__(self):
        self.machines = []

    def add_machine(self, machine):
        self.machines.append(machine)

    def get_total_cost(self):
        total_cost = sum(machine.total_cost for machine in self.machines)
        return total_cost



cloud_service = CloudService()

machine_a = Machine(cloud_service, "Type 1", 2)
machine_b = Machine(cloud_service, "Type 1", 2)
machine_c = Machine(cloud_service, "Type 1", 2)
machine_d = Machine(cloud_service, "Type 2", 5)

machine_a.start_machine()
machine_b.start_machine()
machine_c.start_machine()
machine_d.start_machine()


time.sleep(60)
machine_a.stop_machine()
machine_b.stop_machine()
machine_c.stop_machine()
machine_d.stop_machine()

# Calculate total cost
total_cost = cloud_service.get_total_cost()
print(f"Total cost: ${total_cost:.2f}")