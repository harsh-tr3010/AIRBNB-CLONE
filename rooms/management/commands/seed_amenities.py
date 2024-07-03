from django.core.management.base import BaseCommand
from rooms.models import Amenity

class Command(BaseCommand):

    help = "This Command Creates Amenities"


    def handle(self, *args, **options):
        amenities = [
            "Wifi",
            "Kitchen",
            "Washing machine",
            "Dryer",
            "Air conditioning",
            "Heating",
            "Dedicated workspace",
            "TV",
            "Hair dryer",
            "Iron",
            "Pool",
            "Hot tub",
            "Free parking",
            "EV charger",
            "Cot",
            "King bed",
            "Gym",
            "BBQ grill",
            "Breakfast",
            "Indoor fireplace",
            "Smoking allowed",
            "Beachfront",
            "Waterfront",
            "Smoke alarm",
            "Carbon monoxide alarm",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
