from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm


def index(request):

    # this variable represents the entries in the database
    # I need to import the Entry class
    # Entry.objects.all() get all the Entry objects in that class
    # by changing it to .order_by('-date_posted) they get ordered in descending order, last posted first
    entries = Entry.objects.order_by('-date_posted')

    # context is a dictionary with a key entries and the value is all the entries
    # in the database. Do I can later pass those values to the index.html
    context = {'entries': entries}

    # so now I can pass the context variable to the template
    return render(request, 'entries/index.html', context)


def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = EntryForm()

    context = {'form': form}

    return render(request, 'entries/add.html', context)








