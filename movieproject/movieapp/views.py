from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Movieform
from .models import movie


# Create your views here.


def index(request):
    movievar = movie.objects.all()
    context = {'movielist': movievar}
    return render(request, 'index.html', context)


def details(request, movie_id):
    movie1 = movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie1})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        year = request.POST.get('year')
        movie2 = movie(name=name, desc=desc, img=img, year=year)
        movie2.save()
    return render(request, 'add.html')


def update(request, id):
    movie1 = movie.objects.get(id=id)
    form = Movieform(request.POST or None, request.FILES, instance=movie1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie1})


def delete(request, id):
    if request.method == 'POST':
        movie1 = movie.objects.get(id=id)
        movie1.delete()
        return redirect('/')
    return render(request, 'delete.html')
