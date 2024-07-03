from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as users_models

class AbstractItem(core_models.TimeStampedModel):

    
    name = models.CharField(max_length= 80)


    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    

class RoomType(AbstractItem):

    class Meta:
        verbose_name_plural = "Room Types"


class Amenity(AbstractItem):

    class Meta:
        verbose_name_plural = "Aminities"

class Facility(AbstractItem):

    class Meta:
        verbose_name_plural = "Facilites"

class HouseRule(AbstractItem):

    class Meta:
        verbose_name_plural = "House Rules"



class Room(core_models.TimeStampedModel):

    name = models.CharField(max_length=140)
    description = models.TextField(blank= True)
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.FloatField()
    adress = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(users_models.User, related_name="rooms", on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, related_name="rooms", on_delete= models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank= True)
    facilities = models.ManyToManyField(Facility, related_name="rooms", blank= True)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank= True)


    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)
    

    def total_rating(self):
        all_review = self.reviews.all()
        all_ratings = 0
        if len(all_review) > 0:
            for review in all_review:
                all_ratings += (review.rating_average())
                return all_ratings / len(all_review)
        return 0
    

class Photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey(Room, related_name="photos", on_delete= models.CASCADE)

    def __str__(self):
        return self.caption
