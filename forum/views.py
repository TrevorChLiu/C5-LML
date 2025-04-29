from .form import PostForm, CommentForm, ForumForm
from forum.models import Forum
from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseForbidden
from .models import Post, Comment, Mention
from user.models import User
    
def categories(request):
    if request.method == 'POST':
        form = ForumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('forum:categories')
    else:
        form = ForumForm()
    return render(request, 'forum/new_game.html', {'form': form})

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

def forum(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    order_by = request.GET.get('order_by', '-created_at')
    post_list = forum.posts.all().order_by(order_by)
    paginator = Paginator(post_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Increment the popularity
    viewed_forums = request.session.get('viewed_forums', [])
    if forum_id not in viewed_forums:
        forum.popularity += 1
        forum.save(update_fields=["popularity"])
        viewed_forums.append(forum_id)
        request.session['viewed_forums'] = viewed_forums

    return render(request, 'forum/forum.html', {
        'forum': forum,
        'page_obj': page_obj,
        'order_by': order_by
    })

@login_required
def post_create(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.forum = forum
            post.save()
            return redirect('forum:forum', forum_id=forum_id)
    else:
        form = PostForm()
    return render(request, 'forum/post_form.html', {'form': form, 'forum':forum})

def post_detail(request, forum_id, pk):
    post = get_object_or_404(Post, pk=pk)
    forum = get_object_or_404(Forum, id=forum_id)
    post.views += 1
    post.save()
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('user:index')
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            mentions = extract_mentions(comment.content)
            for username in mentions:
                try:
                    user = User.objects.get(username=username)
                    Mention.objects.create(user=user, comment=comment)
                except User.DoesNotExist:
                    pass
            return redirect('forum:post_detail', pk=pk, forum_id=forum_id)
    else:
        form = CommentForm()
    
    return render(request, 'forum/post_detail.html', {
        'post': post,
        'form': form,
        'comments': post.comments.filter(parent_comment__isnull=True),
        'forum':forum
    })

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({
        'liked': liked,
        'total_likes': post.total_likes()
    })

@login_required
def delete_comment(request, comment_id, forum_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author or request.user.is_superuser:
        comment.delete()
    return redirect('forum:post_detail', pk=comment.post.id, forum_id=forum_id)

@login_required
def delete_post(request, forum_id, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_superuser:
        return HttpResponseForbidden("无权删除此帖子")
    post.delete()
    return redirect('forum:forum', forum_id=forum_id)

def extract_mentions(text):
    import re
    return re.findall(r'@(\w+)', text)