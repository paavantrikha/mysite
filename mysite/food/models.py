from django.db import models

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name # To see item_name(string) instead of object1, object2 when we run Item.objects.all()

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://members.jusbfit247.com/wp-content/uploads/food-placeholder.jpg")