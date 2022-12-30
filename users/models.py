from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # create a one-to-one relationship with the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # create a profile picture field
    image = models.ImageField(
        default='default-profile.jpg', upload_to='profile_pics')
    # tell django how to display the model

    def __str__(self):
        # return the username plus profile
        return f'{self.user.username} Profile'

    # - override the save method to save the image to a smaller size
    # - this is the save method that gets run after the model is saved
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     # open the image of current instance
    #     img = Image.open(self.image.path)

    #     # - resize the image to a fixed size
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         # - save the image again with new dimensions
    #         img.save(self.image.path)
