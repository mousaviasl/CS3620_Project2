from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from random import choice
from .models import MadLibStory
from .forms import MadLibForm

def home(request):
    return render(request, 'MadLibs/home.html')

def create_madlib(request):
    stories = MadLibStory.objects.all()
    selected_story = choice(stories) if stories else None

    if request.method == 'POST':
        form = MadLibForm(request.POST)
        if form.is_valid():
            user_words = form.cleaned_data
            filled_story = selected_story.template.format(**user_words)
            return render(request, 'MadLibs/madlib_result.html', {'story': filled_story})
    else:
        form = MadLibForm()

    return render(request, 'MadLibs/create_madlib.html', {'form': form, 'story': selected_story})

def about(request):
    return render(request, 'MadLibs/about.html')
