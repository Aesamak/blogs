from django.shortcuts import render,redirect
from .models import blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

def blog_list(request):
    blogs = blog.objects.all()
    return render(request, "blog/blog_list.html", {"blogs": blogs})

@login_required
def create_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)  # Include files for image upload
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Set the author to the logged-in user
            blog.save()
            messages.success(request, "Blog post created successfully!")
            return redirect("blog_list")  # Redirect to the blog list view
    else:
        form = BlogForm()

    return render(request, "blog/create_post.html", {"form": form})



def blog_detail(request, blog_id):
    blogs = get_object_or_404(blog, id=blog_id)  # Fetch blog or return 404
    return render(request, "blog/blog_detail.html", {"blog": blogs})


@login_required
def edit_post(request, blog_id):
    blogs = get_object_or_404(blog, id=blog_id)

    if request.user != blogs.author:  
        return redirect("blog_list")  

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blogs)  # Load existing data
        if form.is_valid():
            form.save()
            return redirect("blog_detail", blog_id=blogs.id)  # Redirect to blog details
    else:
        form = BlogForm(instance=blogs)

    return render(request, "blog/edit_post.html", {"form": form, "blog": blogs})


@login_required
def delete_post(request, blog_id):
    blogs = get_object_or_404(blog, id=blog_id)

    if request.user != blogs.author:  # Prevent unauthorized deletion
        return redirect("blog_list")

    if request.method == "POST":  # Confirm deletion
        blogs.delete()
        return redirect("blog_list")  # Redirect to the blog list page

    return render(request, "blog/delete_post.html", {"blog": blogs})
