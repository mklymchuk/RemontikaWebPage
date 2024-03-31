from django.shortcuts import render

def index(request):
    """The home page for company."""
    return render(request, 'company/index.html')