from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('listings', views.listings_json_resp, name='listings_json_resp'),
    path('listing/<int:listing_id>', views.listing_json_resp, name='listing_json_resp'),
]