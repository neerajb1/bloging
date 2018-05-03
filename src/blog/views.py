from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm , ContactForm
def home(request):
    title = "Welcome"
    # if request.user.is_authenticated():
    #     title = "My Title %s" %(request.user)
    # if request.method =="POST":
    #     print request.POST
    template_form = SignUpForm(request.POST or None)

    context = {

    "title" : title ,
    "form" : template_form,

    }


    if template_form.is_valid():
        instance = template_form.save(commit = False)
        full_name = template_form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name

        # if not instance.full_name:
        #     instance.full_name = "Neeraj"
        instance.save()
        print instance.email
        print instance.timestamp
        context = {
        "title" : "Thank you"
        }
    return render(request , "base.html" , context)


def contact(request):
    forms = ContactForm(request.POST or None)

    context = {
    "form" : forms ,
    }

    if forms.is_valid():
        # print forms
        # for key , value in forms.cleaned_data.iteritems():
        #     print key , value
        #     # print forms.cleaned_data.get(key)

        email = forms.cleaned_data.get("email")
        message = forms.cleaned_data.get("message")
        full_name = forms.cleaned_data.get("full_name")
        subject = "Mail checking"
        from_email = settings.EMAIL_HOST_USER
        to_email = [email , "nk.shukla2k18@gmail.com"]
        send_mail(
            subject,
            message,
            from_email,
            to_email,
            fail_silently=False,
            )
        # # print forms.cleaned_data
        # print email , message , full_name

    return render(request , "forms.html" , context)
