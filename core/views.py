from django.shortcuts import render
from forum.models import Forum

# Create your views here.
def home(request):
    top_1_forum = Forum.get_top_1_forum()
    top_5_forums = Forum.get_top_5_forums()
    top_100_forums = Forum.get_top_100_forums()

    return render(request, 'core/home.html', {
        'top1': top_1_forum,
        'top2_to_top5': top_5_forums[1:],
        'top100': top_100_forums
    })
