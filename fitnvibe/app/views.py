from django.shortcuts import render, HttpResponse
from .models import ContactForm
from .models import MembershipPlan
from django.http import JsonResponse

# Create your views here.
def home(request):
    plans = MembershipPlan.objects.all()
    return render(request, "home.html", {'plans': plans})

def membership(request):
    plans = MembershipPlan.objects.all()
    return render(request, "membership.html", {'plans': plans})

def about_us(request):
    return render(request, "about_us.html")

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactForm.objects.create(name=name, email=email, message=message)
        return JsonResponse({'success': True, 'message': 'Thank you for contacting us!'})
    return render(request, 'contact_us.html')

# def membership_plans(request):
#     plans = MembershipPlan.objects.all()
#     return render(request, 'membership.html', {'plans': plans})