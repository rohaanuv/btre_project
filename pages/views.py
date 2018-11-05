from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from  listings.choices import price_choice,bedroom_choices,state_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context ={
        'listings':listings,
        'price_choice':price_choice,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices
    }

    return render(request,'pages/index.html',context)
def about(request):
    #get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    #get sailer of the month
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context ={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }

    return render(request,'pages/about.html', context)