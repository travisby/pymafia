from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
# from django import forms
from pymafia.forms import GameForm, CharacterForm
from django.shortcuts import render


# TODO displaying a form could be a function, taking type as param
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/game/' + GameForm.cleaned_data['game'].id)
    else:
        form = GameForm()

    return render(request, 'contact.html', {
        # this should render a generic detailed view
        'form': form,
    })

@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/game/' + CharacterForm.cleaned_data['game'].id)
    else:
        form = GameForm()

    return render(request, 'contact.html', {
        # this should render a generic detailed view

        'form': form,
    })
