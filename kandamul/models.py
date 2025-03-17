from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=255, default="From the Heart of the Himalayas")
    content = models.TextField()
    
    def __str__(self):
        return self.title


class Testimonial(models.Model):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    designation = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}"

