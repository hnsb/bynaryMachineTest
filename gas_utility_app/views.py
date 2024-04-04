# gas_utility_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_status')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_request_form.html', {'form': form})

@login_required
def request_status(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'request_status.html', {'service_requests': service_requests})
