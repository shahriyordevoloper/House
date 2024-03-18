from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm
from django.db.models import Q



# CRUD - create, retrieve, update, delete, list

def listing_list(request):
    
    # listings = Listing.objects.all().filter(address=data.get('location'))
    listings = Listing.objects.all()
    if request.GET.get('location') != None and  request.GET.get('Min') != None and request.GET.get('Max') != None :
        listings=Listing.objects.all().filter( Q(price__gte=request.GET.get('Min')) & Q(price__lte=request.GET.get('Max')) ).filter()

    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)


def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)


def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)



def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)


def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")
