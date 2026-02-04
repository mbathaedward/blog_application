from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostCreationform
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5, orphans=4,allow_empty_first_page=True)
    page = request.GET.get('page')
    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        paginated_posts = paginator.page(1)
    except EmptyPage:
        paginated_posts = paginated_posts.page(paginator.num_pages)
    title = 'list posts'
    return render(request, 'blog_app/list.html', {'posts':paginated_posts,'title':title})

def post_detail(request,id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog_app/detail.html', {'post':post})

def post_create(request):
    if request.method == 'POST':
        form = PostCreationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PostCreationform()
    title = 'create'
    return render(request,'blog_app/create.html', {'form':form,'title':title})

def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostCreationform(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PostCreationform(instance=post)
        title = 'update'
    return render(request, 'blog_app/update.html',{'form':form,'title':title})

def post_delete(request, id):
    post = get_object_or_404(Post,id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('list')
    title = 'delete'
    return render(request, 'blog_app/delete.html',{'post':post, 'title':title})