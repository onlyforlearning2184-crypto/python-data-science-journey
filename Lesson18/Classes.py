class Vehicle:
    def __init__(self, compeny, model):
        self.compeny = compeny
        self.model = model

    def moves(self):
        print("Moves along....")

    def get_compeny_model(self):
        print(f"My favourite car is {self.compeny} {self.model}.")


class Airplane(Vehicle):
    def __init__(self, compeny, model, faa_id):
        super().__init__(compeny, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along....")


class Boat(Vehicle):
    def moves(self):
        print("Surf along....")


class Cycle(Vehicle):
    pass


my_car = Vehicle("Dodge", "Challanger")
# print(my_car.compeny)
# print(my_car.model)
my_car.get_compeny_model()
my_car.moves()

your_car = Vehicle("Tesla", "Model-3")
your_car.get_compeny_model()

cessna = Airplane("Cessna", "Skyhawk", "N-12345")
mack = Boat("Mack", "Pinnacle")
schannal = Cycle("Schannal", "16-Gear")

cessna.get_compeny_model()
cessna.moves()

mack.get_compeny_model()
mack.moves()

schannal.get_compeny_model()
schannal.moves()

print("\n\n")
# polymorphism is and ability of an object to behave differently based on differnt input
for v in (my_car, your_car, cessna, mack, schannal):
    v.get_compeny_model()
    v.moves()
