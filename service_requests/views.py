from django.shortcuts import render, redirect
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        request_type = request.POST.get('request_type')
        details = request.POST.get('details')
        attachment = request.FILES.get('attachment')
        ServiceRequest.objects.create(request_type=request_type, details=details, attachment=attachment)
        return redirect('track_requests')

    return render(request, 'submit_request.html')

def track_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'track_requests.html', {'requests': requests})
