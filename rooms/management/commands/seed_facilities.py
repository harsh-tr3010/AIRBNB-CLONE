from typing import Any
from django.core.management import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "This Command creates Facilites list"

    def handle(self, *args, **options):
        facilities = [
            "Private Enterance",
            "Paid Parking on Premises",
            "Paid parking off Premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f'{len(facilities)} facilities created'))