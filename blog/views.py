from django.http.response import HttpResponseRedirect, ResponseHeaders
from django.views.generic import ListView
from django.views import View
from django.urls import reverse
from django.shortcuts import render

from .models import Post
from .forms import CommentForm


def get_date(post):
    return post['date']
    
# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset =  super().get_queryset()
        data = queryset[:3]
        return data

    

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts":all_posts
#     })


class SinglePostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
          "post": post,
          "post_tags": post.caption.all(),
          "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):    
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit= False)
            comment.post = post
            comment .save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        else:  
            context = { 
            "post":post,
            "post_tag": post.caption.all(),
            "comment_form": CommentForm
            }
            return render(request, "blog/post-detail.html", context)


# def post_detail(request, slug):

    
    
#     identfied_post = get_object_or_404(Post, slug = slug) 
    
#     return render(request, "blog/post-detail.html", {
#         "post": identfied_post,
#         "post_tags": identfied_post.caption.all()
#     })
