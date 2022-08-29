from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def success(request):
    return render(request, 'success.html')
