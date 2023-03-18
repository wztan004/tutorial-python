# Source: ChatGPT

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print("Engine started")

class Transmission:
    def __init__(self, num_gears):
        self.num_gears = num_gears

    def shift_up(self):
        print("Shifting up")

    def shift_down(self):
        print("Shifting down")

class Car:
    def __init__(self, engine_horsepower, transmission_num_gears):
        self.engine = Engine(engine_horsepower)
        self.transmission = Transmission(transmission_num_gears)

    def start(self):
        self.engine.start()
        print("Car started")

    def accelerate(self):
        self.transmission.shift_up()
        print("Accelerating")

    def brake(self):
        self.transmission.shift_down()
        print("Braking")


if __name__ == "__main__":
    my_car = Car(engine_horsepower=200, transmission_num_gears=6)
    my_car.start()
    my_car.accelerate()
    my_car.brake()
    