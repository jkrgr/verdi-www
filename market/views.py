# Create your views here.
from django.shortcuts import render

def portfolio_view(request):
    return render(request, 'portfolio.html', {'stocks':['STL','HLNG','BAKKA']})