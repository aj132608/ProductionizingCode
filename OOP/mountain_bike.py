from bicycle import Bicycle


class MountainBike(Bicycle):
    def __init__(self):
        # Add any attributes unique to a mountain bike

        # Calls the constructor of the base Bicycle class
        super().__init__()

    # Add specific methods for a mountain bike that are
    # called instead of the methods in the Bicycle class
    def change_cadence(self, new_val):
        self.cadence = new_val

    def change_gear(self, new_val):
        self.gear = new_val

    def speed_up(self, increment):
        self.speed += increment

    def apply_breaks(self, decrement):
        self.speed -= decrement

