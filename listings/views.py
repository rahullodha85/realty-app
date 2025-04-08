from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'listings/listings.html')

def search(request):
    return render(request, 'listings/search.html')

def listing(request, listing_id):
    return render(request, 'listings/listing.html', {'listing_id': listing_id})