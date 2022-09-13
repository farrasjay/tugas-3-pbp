from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_barang_katalog,
        'nama': 'Farras Hafizhudin Indra Wijaya',
        'npm' : '2106652682'
    }
    return render(request, "katalog.html", context)