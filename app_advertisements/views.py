from .models import Advertisements
from .forms import AdvertisementForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
def index(request):
    advertisements = Advertisements.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_advertisements/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisements = Advertisements(**form.cleaned_data)
            advertisements.user = request.user
            advertisements.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)

def advertisement_detail(request, pk):
    advertisement = Advertisements.objects.get(id=pk)
    context = {
        'advertisement': advertisement}
    return render(request, 'app_advertisements/advertisement.html', context)
def my_advertisements(request):
    advertisements = Advertisements.objects.filter(user=request.user)
    context = {'advertisements': advertisements}
    return render(request, 'app_advertisements/my_advertisements.html', context)
@login_required(login_url=reverse_lazy('login'))
def advertisement_edit(request, pk):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisements = Advertisements(**form.cleaned_data)
            advertisements.user = request.user
            advertisements.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-edit.html', context)

# Create your views here.
