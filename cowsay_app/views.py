from django.shortcuts import render, redirect
from cowsay_app.forms import CowsayForm
from cowsay_app.models import Cowsay
import subprocess



def insert_view(request):
    if request.method == 'POST':
        form = CowsayForm(request.POST)
        if form.is_valid():
            name = request.POST['cowsay_string']
            form.save()
            string = subprocess.check_output(
                ['cowsay', name], universal_newlines=True)
            return render(request, 'index.html', {'name': string})
    return render(request, 'index.html')


def history(request):
    moo_history = Cowsay.objects.values('cowsay_string').order_by('-id')[:10]
    mooList = []
    
    for item in moo_history:
        string = subprocess.check_output(
            ['cowsay', item['cowsay_string']], universal_newlines=True)
        mooList.append(string)

    return render(request, 'history.html', {'cowsay_list': mooList})
