class Bicycle:

    def __init__(self, cadence=0, speed=0, gear=1):
        self.cadence = cadence
        self.speed = speed
        self.gear = gear

    def change_cadence(self, new_val):
        self.cadence = new_val

    def change_gear(self, new_val):
        self.gear = new_val

    def speed_up(self, increment):
        self.speed += increment

    def apply_breaks(self, decrement):
        self.speed -= decrement

    def __str__(self):
        return f"cadence: {self.cadence}\nspeed: {self.speed}\ngear: {self.gear}"


if __name__ == "__main__":
    bike_1 = Bicycle()
    bike_2 = Bicycle()

    bike_1.change_cadence(50)
    bike_1.speed_up(10)
    bike_1.change_gear(2)
    print(bike_1)

    bike_2.change_cadence(50)
    bike_2.speed_up(10)
    bike_2.change_gear(2)
    bike_2.change_cadence(40)
    bike_2.speed_up(10)
    bike_2.change_gear(3)
    print(bike_2)
