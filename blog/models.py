from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
#    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.title