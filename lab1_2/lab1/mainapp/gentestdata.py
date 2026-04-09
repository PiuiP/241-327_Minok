import random, string, datetime
from .models import *
from django.db import transaction
import faker
from faker import Faker

fk = Faker()

def gentestdata():
    with transaction.atomic():
        for i in range(1000):
            newPlant = Plant()
            newPlant.name = fk.word()
            newPlant.price = round(random.uniform(100, 5000), 2)
            newPlant.height_cm = random.randint(10, 300)
            newPlant.is_evergreen = random.choice([True, False])
            newPlant.save()
    print("OK gentestdata")