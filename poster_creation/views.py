from django.shortcuts import render
# from matplotlib.style import context

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)