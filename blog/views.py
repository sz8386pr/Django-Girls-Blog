from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# finds posts that are published and the return value is saved as posts. renders main page with posts.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# individual post detail page.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# posting new form.
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():     # if valid. Currently, as long as the title & test fields are not empty
            post = form.save(commit=False)  # don't save it yet
            post.author = request.user  # set the author as user
            post.save()     # and THEN save with the title & text from the form
            return redirect('post_detail', pk=post.pk)  # redirect to post detail page that's just been posted
    else: # by default, display an empty form
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# edit an existing post accessed from the post detail view
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


# lists of UNpublished posts
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


# publish the post
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


# delete the post
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
