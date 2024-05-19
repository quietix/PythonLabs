from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    def operate_car(self):
        self.start_engine()
        self.drive()
        self.stop_engine()


# Легковий
class PassengerCar(Car):
    def start_engine(self):
        print("Starting the engine of the passenger car.")

    def stop_engine(self):
        print("Stopping the engine of the passenger car.")

    def drive(self):
        print("Driving the passenger car.")


# Вантажний
class Truck(Car):
    def start_engine(self):
        print("Starting the engine of the truck.")

    def stop_engine(self):
        print("Stopping the engine of the truck.")

    def drive(self):
        print("Driving the truck.")

    def load_cargo(self):
        print("Loading cargo onto the truck.")

    def operate_car(self):
        self.load_cargo()
        super().operate_car()


# Пасажирський
class Bus(Car):
    def start_engine(self):
        print("Starting the engine of the bus.")

    def stop_engine(self):
        print("Stopping the engine of the bus.")

    def drive(self):
        print("Driving the bus.")

    def board_passengers(self):
        print("Boarding passengers onto the bus.")

    def operate_car(self):
        self.board_passengers()
        super().operate_car()


if __name__ == "__main__":
    passenger_car = PassengerCar()
    truck = Truck()
    bus = Bus()

    print("Passenger Car Operation:")
    passenger_car.operate_car()

    print("\nTruck Operation:")
    truck.operate_car()

    print("\nBus Operation:")
    bus.operate_car()