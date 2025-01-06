from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from django.shortcuts import render, redirect, get_object_or_404
from .models import Clothing
from .forms import ClothingForm
from django.contrib.auth.decorators import login_required

@login_required
@login_required

def clothing(request):
    clothing = Clothing.objects.all()
    con = {
        'clothing': clothing  # Change this t     o 'hom' to match the template
    }
    return render(request, template_name='clothing/allclothing.html', context=con)


def clothing_list(request):
    if request.user.user_type == 'renter':
        # Renters should only see general house information
        clothing = Clothing.objects.all().select_related('owner')  # Select owner to avoid extra queries
    else:
        # Owners should only see their own houses
        clothing = Clothing.objects.filter(owner=request.user)

    return render(request, 'clothing/clothing_list.html', {'clothing': clothing})
@login_required
def clothing_create(request):
    if request.user.user_type != 'owner':
        return redirect('clothing_list')
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES)
        if form.is_valid():
            house = form.save(commit=False)
            house.owner = request.user
            house.save()
            return redirect('clothing_list')
    else:
        form = ClothingForm()
    return render(request, 'clothing/clothing_form.html', {'form': form})

@login_required
def clothing_edit(request, pk):
    house = get_object_or_404(Clothing, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES, instance=house)
        if form.is_valid():
            form.save()
            return redirect('clothing_list')
    else:
        form = ClothingForm(instance=house)
    return render(request, 'clothing/clothing_form.html', {'form': form})

@login_required
def clothing_delete(request, pk):
    house = get_object_or_404(Clothing, pk=pk, owner=request.user)
    house.delete()
    return redirect('clothing_list')

def clothing_detail(request, pk):
    clothing = get_object_or_404(Clothing, pk=pk)
    is_owner = clothing.owner == request.user  # Assuming the Clothing model has an 'owner' field

    context = {
        'clothing': clothing,
        'is_owner': is_owner,
    }
    return render(request, 'clothing/clothing_detail.html', context)

# def contact_owner(request, pk):
#     clothing = get_object_or_404(Clothing, pk=pk)  # Fetch the clothing item using the primary key
#     owner = clothing.owner  # Assuming 'owner' is a ForeignKey field in the Clothing model
#
#     context = {
#         'clothing': clothing,  # Pass the clothing item to the template
#         'owner': owner,        # Pass the owner details to the template
#     }
#     return render(request, 'clothing/allclothing.html', context)