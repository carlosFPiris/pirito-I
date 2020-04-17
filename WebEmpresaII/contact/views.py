from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage


def contact(request):
    contact_form = ContactForm()
    print("Tipo de peticion: {}".format(request.method))
    if request.method == "POST":
        contact = ContactForm(data=request.POST)
        if contact.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            return redirect(reverse('contact')+"?ok")
            email = EmailMessage(
                "Bikephilosophy contact",
                "De {} con email: {} escribió\n\n {}".format(
                    name, email, content),
                "bike-6902c0@inbox.mailtrap.io",
                ["esteesdestino@yahoo.es"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form': contact_form})
