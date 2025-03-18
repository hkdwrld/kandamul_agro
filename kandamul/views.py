from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import AboutUs, Testimonial
from product.models import Product
from .forms import ContactForm

def index_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact = form.save()
            
            # Send email to admin
            subject = f"New Contact Form Submission: {contact.subject}"
            message = f"""
            Name: {contact.name}
            Email: {contact.email}
            Subject: {contact.subject}
            
            Message:
            {contact.message}
            """
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.ADMIN_EMAIL]
            
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Your message has been sent successfully!')
            print("Email sent successfully")  # Debug print
            
            
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