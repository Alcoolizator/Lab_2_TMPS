from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def drive(self):
        pass


class Engine(ABC):
    pass


class Wheels(ABC):
    pass


class LuxuryEngine(Engine):
    pass


class LuxuryWheels(Wheels):
    pass


class SportsEngine(Engine):
    pass


class SportsWheels(Wheels):
    pass


class Sedan(Car):
    def __init__(self, engine, wheels):
        self.engine = engine
        self.wheels = wheels

    def drive(self):
        print("Driving a Sedan with {} and {}.".format(
            type(self.engine).__name__, type(self.wheels).__name__))


class SportsCar(Car):
    def __init__(self, engine, wheels):
        self.engine = engine
        self.wheels = wheels

    def drive(self):
        print("Driving a Sports car with {} and {}.".format(
            type(self.engine).__name__, type(self.wheels).__name__))


class CarDealership(ABC):
    @abstractmethod
    def order_car(self, car_type):
        pass


class LuxuryCarDealership(CarDealership):
    def order_car(self, car_type):
        if car_type == "sedan":
            return Sedan(LuxuryEngine(), LuxuryWheels())
        elif car_type == "sports car":
            return SportsCar(LuxuryEngine(), LuxuryWheels())
        else:
            raise ValueError("Invalid car type.")


class SportsCarDealership(CarDealership):
    def order_car(self, car_type):
        if car_type == "sedan":
            return Sedan(SportsEngine(), SportsWheels())
        elif car_type == "sports car":
            return SportsCar(SportsEngine(), SportsWheels())
        else:
            raise ValueError("Invalid car type.")


def main():
    car_dealership_type = input("Enter car dealership type (luxury or sports): ")
    if car_dealership_type.lower() == "luxury":
        car_dealership = LuxuryCarDealership()
    elif car_dealership_type.lower() == "sports":
        car_dealership = SportsCarDealership()
    else:
        print("Invalid input. Exiting...")
        return

    car_type = input("Enter car type (sedan or sports car): ")
    if car_type.lower() == "sedan":
        car = car_dealership.order_car("sedan")
    elif car_type.lower() == "sports car":
        car = car_dealership.order_car("sports car")
    else:
        print("Invalid input. Exiting...")
        return

    car.drive()


if __name__ == '__main__':
    main()
