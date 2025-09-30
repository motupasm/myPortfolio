from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.


def index(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        send_mail(
            f"We recieved your message!",
            f"Hello {name},\n\n"
            f"Thanks for contacting us. Here’s what you sent:\n\n"
            f"Subject: {subject}\n"
            f"Message: {message}\n\n"
            f"We’ll reply soon!",
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        messages.success(request , 'Your message was successfully sent')
        # to me(admin)
        send_mail(
            f"New message from {name}",
            f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}",
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL], 
            fail_silently=False, 
        )
        return redirect("index")

    return render(request, "index.html")
