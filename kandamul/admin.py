from django.contrib import admin
from .models import AboutUs, Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'message', 'designation', 'created_at')  
    search_fields = ('name', 'message')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')  