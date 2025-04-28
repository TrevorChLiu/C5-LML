from django.shortcuts import render, redirect

from .form import ForumForm
from forum.models import Forum
from django.db.models import Q
    
def categories(request):
    if request.method == 'POST':
        form = ForumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('forum:categories')
    else:
        form = ForumForm()
    return render(request, 'forum/categories.html', {'form': form})

def all_games(request):
    games = Forum.get_all_forums_sorted_by_name
    return render(request, "forum/all_games.html", {
        'games': games
    })

def leaderboard(request):
    games = Forum.get_all_forums_sorted_by_popularity
    return render(request, "forum/all_games.html", {
        'games': games
    })

def results(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Forum.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    return render(request, 'forum/results.html', {
        'query': query,
        'results': results
    })