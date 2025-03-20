from django.shortcuts import render, redirect

from django.conf import settings
from django.contrib import messages

from kandamul.utils import send_background_mail
from .models import AboutUs, Testimonial
from product.models import Product
from .forms import ContactForm

def index_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact = form.save()

            subject = f"New Contact Form Submission: {contact.subject}"
            message = f"""
            Name: {contact.name}
            Email: {contact.email}
            Subject: {contact.subject}
            Message:{contact.message}
            """
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.ADMIN_EMAIL]
            send_background_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('kandamul:home')  # Use named URL pattern
    else:
        form = ContactForm()
    
    # Prepare context data
    context = {
        'form': form,
        'about_content': AboutUs.objects.first(),
        'products': Product.objects.all(),
        'testimonials': Testimonial.objects.all()
    }
    
    return render(request, 'index.html', context)