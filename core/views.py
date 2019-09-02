from django.shortcuts import render
from .models import *

# Create your views here.

def contact(request):
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        msg_r = request.POST.get('message')
        c= Contact(name=name_r,email=email_r,message=msg_r)
        c.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'home.html')

def home(request):
    about = About.objects.first()
    service = Service.objects.all()
    recentwork = RecentWork.objects.all()
    client = Client.objects.all()
    context = {'about':about, 'services':service,'works':recentwork,'client':client}
    return render(request, 'home.html',context)
