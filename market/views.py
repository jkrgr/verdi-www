# Create your views here.
from django.shortcuts import render

def portfolio_view(request):
    return render(request, 'portfnolio.html', {'stocks':['STL','HLNG','BAKKA']})