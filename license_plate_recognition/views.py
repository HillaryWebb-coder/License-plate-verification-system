from django.shortcuts import render
from .models import Log
from .forms import LogForm
# Create your views here.

def CreateLog(request):

    form = LogForm()

    if request.method == 'POST':
        form = LogForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = LogForm()
    
    return render('home.html', {'form': form})