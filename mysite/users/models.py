from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    #OnetoOne means one profile will be associated with one User and once User is deleted, profile will also be deleted but not vice versa.
    #on_delete=models.CASCADE - If User is deleted, associated Profile willalso be deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Once User is deleted, profile will also be deleted but not vice versa.
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures') #upload_to gives name of directory where default image is uploaded
    location = models.CharField(max_length=100)

# Below def __str__(self): controls how the model objects are represented in Django's administrative interface(admin.site) and 
# other areas where the model objects are displayed. It helps to provide a meaningful and human-readable representation of the object.
    def __str__(self): # String representation of the model. To access objects in the model. 
        return self.user.username # To get the username
