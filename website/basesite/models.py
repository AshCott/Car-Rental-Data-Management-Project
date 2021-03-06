from django.db import models



# Create your models here.


# Store Information Table
class Store(models.Model):
    STATE_CHOICES = [('QLD', 'Queensland'),
                     ('NSW', 'New South Wales'),
                     ('VIC', 'Victoria'),
                     ('ACT', 'Australian Capital Territory'),
                     ('TAS', 'Tasmania'),
                     ('SA', 'South Australia'),
                     ('WA', 'Western Australia'),
                     ('NT', 'Northen Territory')]
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    city = models.CharField(max_length=50)
    state = models.CharField(choices=STATE_CHOICES, max_length=25)


# Customer Information Table
class Customer(models.Model):
    SEX_CHOICES = [('M', 'Male'),
                   ('F', 'Female')]
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    birthday = models.DateField()
    occupation = models.CharField(max_length=100)
    gender = models.CharField(choices=SEX_CHOICES, max_length=1)

    # Queryset -> Json
    def JSonObject(self):
        data = {'id': self.id, 'name': self.name, 'phone': self.phone, 'address': self.address,
        'birthday': self.birthday, 'occupation': self.occupation, 'gender': self.gender}
        return data



# Car Information Table
class Car(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    year = models.IntegerField()
    purchase_price = models.IntegerField()
    engine_size = models.DecimalField(decimal_places=1,max_digits=3)  # 2.5L - Numb only the L is removed
    fuel_system = models.CharField(max_length=50)
    tank_capacity = models.IntegerField()  # 82L - Numb only the L is removed
    power = models.IntegerField()  # 140Kw - Numb only the Kw is removed
    seating_capacity = models.IntegerField()
    transmission = models.CharField(max_length=10)
    body_type = models.CharField(max_length=30)
    drive = models.CharField(max_length=3)
    wheelbase = models.IntegerField()  # 2550mm - Numb only the mm is removed

    # Queryset -> Json
    def JSonObject(self):
        data = {'id': self.id, 'name': self.name, 'model': self.model, 'series': self.series,
        'year': self.year, 'purchase_price': self.purchase_price, 'engine_size': self.engine_size,
        'fuel_system': self.fuel_system, 'tank_capacity': self.tank_capacity,
        'power': self.power, 'seating_capacity': self.seating_capacity,
        'transmission': self.transmission, 'body_type': self.body_type,
        'drive': self.drive, 'wheelbase': self.wheelbase, 'current_store': self.currentStore()}
        return data

    # Currently only body type similarity
    def similar(self):
        results = Car.objects.filter(body_type__icontains=self.body_type)[:3]
        return [result.JSonObject() for result in results]

    # Rental history of a specific car. Returns queryset to be used on car_details page
    def history(self):
        results = Order.objects.filter(carID=self.id).order_by('-pickup_date')
        return results

    # Returns current store of the car
    def currentStore(self):
        results = Order.objects.filter(carID=self.id).order_by('-return_date')
        return results[0].return_store.name


# List of history of car rentals
class Order(models.Model):
    date = models.DateField()
    pickup_date = models.DateField()
    pickup_store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='pickup_store')
    return_date = models.DateField(blank=True)
    return_store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, related_name='return_store')
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    carID = models.ForeignKey(Car, on_delete=models.CASCADE)
    unavailable =  models.BooleanField(default=False)

    # Helper method to convert object to Json
    def JSonObject(self):
        data = {'date': self.date, 'pickup_date': self.pickup_date,
        'pickup_store': self.pickup_store.name, 'return_store': self.return_store.name,
        'customerID': self.customerID, 'unavailable': self.unavailable}
        return data
