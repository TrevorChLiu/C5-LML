from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "user"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login_view"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path('logout/', LogoutView.as_view(next_page='core:home'), name='logout'),
    path("other_profile/<int:user_id>", views.other_profile, name="other_profile"),
    path("toggle_follow/<int:user_id>/", views.toggle_follow, name="toggle_follow"),
]
