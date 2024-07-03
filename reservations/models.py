from django.db import models
from django.utils import timezone
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampedModel):


    STATUS_PEDING = "Pending"
    STATUS_CONFIRMED = "Confirmed"
    STATUS_CANCCEL = "Cancelled"


    STATUS_CHOICES = (
        (STATUS_PEDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCCEL, "Cancelled")
    )

    status = models.CharField(max_length=12, choices= STATUS_CHOICES, default=STATUS_PEDING)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", related_name="reservations", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)


    def __str(self):
        return f"{self.room} - {self.check_in}"
    

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out
    
    in_progress.boolean = True


    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out
    
    is_finished.boolean = True
    
    is_finished.short_description = "Completed"
        
