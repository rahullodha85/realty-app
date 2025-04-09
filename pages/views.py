from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from listings.models import Listing
from listings.choices import bedroom_choices, price_choices, state_choices
from realtors.models import Realtor
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    context = {
        'realtors': realtors,
        'mvp_realtors': realtors.filter(is_mvp=True),
    }

    return render(request, 'pages/about.html', context)