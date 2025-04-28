from django.urls import path

from . import views

app_name = "forum"
urlpatterns = [
    path("new_game", views.categories, name="categories"),
    path("all_games", views.all_games, name="all_games"),
    path("leaderboard", views.leaderboard, name="leaderboard"),
    path("results", views.results, name="results"),
]