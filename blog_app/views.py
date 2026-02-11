from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostCreationform
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# ---------------------------
# List all posts with pagination
# ---------------------------
def post_list(request):
    posts = Post.objects.all().order_by('-date_created')  # order by newest first
    paginator = Paginator(posts, 5, orphans=4, allow_empty_first_page=True)
    page = request.GET.get('page')

    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        paginated_posts = paginator.page(1)
    except EmptyPage:
        paginated_posts = paginator.page(paginator.num_pages)

    title = 'List Posts'
    return render(request, 'blog_app/list.html', {'posts': paginated_posts, 'title': title})


# ---------------------------
# View a single post
# ---------------------------
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog_app/detail.html', {'post': post})


# ---------------------------
# Create a new post
# ---------------------------

def post_create(request):
    if request.method == 'POST':
        form = PostCreationform(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # must be logged in
            post.save()
            return redirect('list')
        else:
            print(form.errors)  # optional: print form errors for debugging
    else:
        form = PostCreationform()

    return render(request, 'blog_app/create.html', {'form': form, 'title': 'create'})


# ---------------------------
# Update an existing post
# ---------------------------
@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    # Optional: prevent users from editing posts they don't own
    if post.author != request.user:
        return redirect('list')

    if request.method == 'POST':
        form = PostCreationform(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PostCreationform(instance=post)

    return render(request, 'blog_app/update.html', {'form': form, 'title': 'update'})


# ---------------------------
# Delete a post
# ---------------------------
@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    # Optional: prevent users from deleting posts they don't own
    if post.author != request.user:
        return redirect('list')

    if request.method == 'POST':
        post.delete()
        return redirect('list')

    return render(request, 'blog_app/delete.html', {'post': post, 'title': 'delete'})
