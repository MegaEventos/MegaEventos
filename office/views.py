from django.shortcuts import render
from clients.models import Clients
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    clients = Clients.objects.all()
    # clients = Clients.objects.filter()
    print(clients)
    return render(request, 'index.html', {'clients':clients})


# def Office(request):
#     profile = Profile.objects.filter(referenceID=request.user.profile.id)
#     socio = Profile.objects.filter(id=request.user.profile.referenceID)
#     level = Level.objects.all()
#     return render(request,'office/office.html', {'profile':profile,'socio':socio, 'level':level})