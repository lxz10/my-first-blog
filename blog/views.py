from django.shortcuts import render, get_object_or_404
from .models import Post, Resume
from django.utils import timezone
from blog.forms import PostForm, ResumeForm
from django.shortcuts import redirect


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def resume_detail(request, pk):
    resumes = Resume.objects.filter(name__lte='Lauren Alie')
    return render(request, 'blog/resume_detail.html', {'resumes': resumes})

def resume_edit(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    if request.method == "POST":
        resume_form = ResumeForm(request.POST, instance=resume)
        if resume_form.is_valid():
            resume = resume_form.save(commit=False)
            resume.save()
            return redirect('resume_detail', pk=resume.pk)
    else:
        resume_form = ResumeForm(instance=resume)
    return render(request, 'blog/resume_edit.html', {'resume_form': resume_form})
