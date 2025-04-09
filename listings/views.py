from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from listings.choices import bedroom_choices, price_choices, state_choices
from listings.models import Listing


# Create your views here.

def index(request):
    listings = Listing.objects.all().order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)

    page = request.GET.get('page')

    page_listings = paginator.get_page(page)

    context = {
        'listings': page_listings,
    }

    return render(request, 'listings/listings.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': queryset_list,
        'values': request.GET,
    }
    return render(request, 'listings/search.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing.html', context)

def listing_json_resp(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)

    listing_json = serializers.serialize('json', [listing])

    return HttpResponse(listing_json, content_type='application/json')

def listings_json_resp(request):
    listings = Listing.objects.all()

    listings_json = serializers.serialize('json', listings)

    return HttpResponse(listings_json, content_type='application/json')