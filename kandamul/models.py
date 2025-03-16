from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=255, default="From the Heart of the Himalayas")
    content = models.TextField()
    
    def __str__(self):
        return self.title

