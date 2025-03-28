from django.shortcuts import render

# Create your views here.
def excess(request):
    return render(request,'excess_page.html')