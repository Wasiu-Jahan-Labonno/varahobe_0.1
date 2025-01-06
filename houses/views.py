from django.shortcuts import render

# Create your views here.
# houses/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import House
from .forms import HouseForm
from django.contrib.auth.decorators import login_required

@login_required
@login_required

def home(request):
    houses = House.objects.all()
    con = {
        'houses': houses  # Change this t     o 'hom' to match the template
    }
    return render(request, template_name='house/index.html', context=con)


def allhouse(request):
    houses = House.objects.all()
    con = {
        'houses': houses  # Change this t     o 'hom' to match the template
    }
    return render(request, template_name='house/house.html', context=con)

def house_list(request):
    if request.user.user_type == 'renter':
        # Renters should only see general house information
        houses = House.objects.all().select_related('owner')  # Select owner to avoid extra queries
    else:
        # Owners should only see their own houses
        houses = House.objects.filter(owner=request.user)

    return render(request, 'house/house_list.html', {'houses': houses})
@login_required
def house_create(request):
    if request.user.user_type != 'owner':
        return redirect('house_list')
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            house = form.save(commit=False)
            house.owner = request.user
            house.save()
            return redirect('house_list')
    else:
        form = HouseForm()
    return render(request, 'house/house_form.html', {'form': form})

@login_required
def house_edit(request, pk):
    house = get_object_or_404(House, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES, instance=house)
        if form.is_valid():
            form.save()
            return redirect('house_list')
    else:
        form = HouseForm(instance=house)
    return render(request, 'house/house_form.html', {'form': form})

@login_required
def house_delete(request, pk):
    house = get_object_or_404(House, pk=pk, owner=request.user)
    house.delete()
    return redirect('house_list')

@login_required
def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    is_owner = house.owner == request.user

    context = {
        'house': house,
        'is_owner': is_owner,
    }
    return render(request, 'house/house_detail.html', context)

def contact_owner(request, pk):
    house = get_object_or_404(House, pk=pk)
    owner = house.owner  # Assuming 'owner' is the ForeignKey field in House model linking to User

    context = {
        'house': house,
        'owner': owner,
    }
    return render(request, 'house/contact.html', context)