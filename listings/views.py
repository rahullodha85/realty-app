from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    return render(request, 'listings/search.html')

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