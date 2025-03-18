from django.contrib import admin
from .models import AboutUs, Testimonial, ContactMessage

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'message', 'designation', 'created_at')  
    search_fields = ('name', 'message')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')  

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)