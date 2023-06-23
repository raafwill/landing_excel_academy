from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from landingPage.forms import LeadForm
from django.contrib import messages

# def index(request):
#     return render(request, "home.html")


def postLead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Recebemos o seu contato com sucesso! Em breve retornaremos.')
            return redirect('/landing')

    else:
        form = LeadForm()

    return render(request, "home.html", {"form": form})