from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm

def band_list(request):
    bands = Band.objects.all()

    return render(request, 
                  'listings/band_list.html', 
                  {'bands': bands})


def band_detail(request, band_id):  
    band = Band.objects.get(id=band_id)

    return render(request,
                 'listings/band_detail.html',
                 {'band': band}) 

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()

            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    
    return render(request, 'listings/band_create.html', {'form': form})
    
def band_update(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_update.html', {'form': form})

def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    return render(request, 'listings/band_delete.html', {'band': band})



def listings_list(request):
    listings = Listing.objects.all()
    return render(request, 
                  'listings/listing_list.html', 
                  {'listings': listings})

def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 
                  'listings/listing_detail.html', 
                  {'listing': listing})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
        else:
            form = ListingForm()        
    else :
        form = ListingForm() 
    
    return render(request, 'listings/listing_create.html', {'form': form})


def listing_update(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(request, 'listings/listing_update.html', {'form': form})


def contact(request):

    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
            
            return redirect('email-sent')
    else:    
        form = ContactUsForm()

    return render(request, 
                  'listings/contact.html',
                  {'form': form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')


def about(request):
    return render(request, 'listings/about-us.html')