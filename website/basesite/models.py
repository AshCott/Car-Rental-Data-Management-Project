from django.db import models

# Create your models here.


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
    phone = models.CharField(max_length=25)
    city = models.CharField(max_length=50)
    state = models.CharField(choices=STATE_CHOICES, max_length=25)


class Customer(models.Model):
    SEX_CHOICES = [('M', 'Male'),
                   ('F', 'Female')]
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    birthday = models.DateField()
    occupation = models.CharField(max_length=100)
    gender = models.CharField(choices=SEX_CHOICES, max_length=1)


class Car(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    year = models.IntegerField()
    purchase_price = models.IntegerField()
    engine_size = models.IntegerField()  # 2.5L - Numb only the L is removed
    fuel_system = models.CharField(max_length=50)
    tank_capacity = models.IntegerField()  # 82L - Numb only the L is removed
    power = models.IntegerField()  # 140Kw - Numb only the Kw is removed
    seating_capacity = models.IntegerField()
    transmission = models.CharField(max_length=10)
    body_type = models.CharField(max_length=30)
    drive = models.CharField(max_length=3)
    wheelbase = models.IntegerField()  # 2550mm - Numb only the mm is removed


class Order(models.Model):
    date = models.DateField()
    pickup_date = models.DateField()
    pickup_store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='pickup_store')
    return_date = models.DateField(blank=True)
    return_store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, related_name='return_store')
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    carID = models.ForeignKey(Car, on_delete=models.CASCADE)
