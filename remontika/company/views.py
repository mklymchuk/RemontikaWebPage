from django.shortcuts import render

from .models import Service

def index(request):
    """The home page for company."""
    return render(request, 'company/index.html')

def services(request):
    # Query all services from the database
    all_services = Service.objects.all()

    # Pass the services data to the template for rendering
    context = {'services': all_services}
    return render(request, 'company/services.html', context)
