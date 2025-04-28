from django.urls import path

from . import views

app_name = "forum"
urlpatterns = [
    path("new_game", views.categories, name="categories"),
    path("all_games", views.all_games, name="all_games"),
    path("leaderboard", views.leaderboard, name="leaderboard"),
    path("results", views.results, name="results"),
    path('forum/<int:forum_id>', views.forum, name='forum'),
    path('post/new/<int:forum_id>', views.post_create, name='post_create'),
    path('<int:forum_id>/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:forum_id>/post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('<int:forum_id>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]