class vehicle:
    def __intit__(self, make, model, Model_Variant, year, fuel_type, model_type):
        self.make = make
        self.model = model
        self.year = year
        self.fueltype = fuel_type
        self.model_type = model_type

class Car(vehicle):
    def __intit__(self, make, model, Model_Variant, year, fuel_type, model_type, odometer):
        super().__init__(make, model, Model_Variant, year, fuel_type, model_type)

def return_info(self):
    return super().return_info() + f'Make: {self.make}, Model: {self.model}, Variant: {self.Model_Variant}, Year: {self.year}'


Silvia = Car('Nissian', 'Silvia', 'S15', 2000, 'E85', 'Coupe', 200000)
Falcon = Car('ford', 'G6E', 'NA', 2014, 'Petrol' 'Sedan', 175000)

garage = [Silvia, Falcon]
for vehicle in garage:
     print(vehicle.return_info())