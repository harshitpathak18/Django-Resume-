from django.shortcuts import render

# Create your views here.
def exp(request):
    return render(request,'exp/exp.html')