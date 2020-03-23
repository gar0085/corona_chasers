from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import RegistrationForm
from .models import Comment, Country, Profile
from .scraper import pop_database

pop_database() 


class CommentCreate(CreateView):
    model = Comment
    fields = '__all__'


class CommentUpdate(UpdateView):
    model = Comment
    fields = ['posted_at', 'content']


class CommentDelete(DeleteView):
    model = Comment
    success_url = '/countries/<int:country_id>/'


def profile(request):
    return render(request, 'profile.html')
    

def home(request):
    return render(request, 'home.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = RegistrationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def countries_index(request):
    return render(request, 'countries/index.html')


def countries_detail(request, country_id):
    return render(request, 'countries/detail.html')


def profiles_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profile.html', {'user': profile.user})


def assoc_country(request, profile, country_id):
    pass


def unassoc_country(request, profile, country_id):
    pass


class CountryList(ListView):
    model = Country
