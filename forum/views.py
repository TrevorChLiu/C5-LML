from django.shortcuts import render, redirect

from .form import ForumForm

    
def categories(request):
    if request.method == 'POST':
        form = ForumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('forum:categories')
    else:
        form = ForumForm()
    return render(request, 'forum/categories.html', {'form': form})
