from django.shortcuts import render

def example(request):
    return render(request, "leaderboard/example.html")