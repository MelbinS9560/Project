from django.shortcuts import render

# Create your views here.
def Donation(request):
    return  render(request,'donation_page.html')