from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, View
from posts.models import BlogPost
from django.urls import reverse_lazy
from posts.forms import BlogPostForm
from django.shortcuts import redirect, get_object_or_404

class BlogHome(ListView):
    model = BlogPost
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)

class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = 'posts/blogpost_create.html'
    form_class = BlogPostForm  # Utilise le formulaire

class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = 'posts/blogpost_edit.html'
    form_class = BlogPostForm  # Utilise le formulaire

class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = 'post'

class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = 'post'
    template_name = 'posts/blogpost_confirm_delete.html'  
    success_url = reverse_lazy('posts:home')

class BlogPostPublishToggle(View):
    def post(self, request, slug):
        post = get_object_or_404(BlogPost, slug=slug)
        post.published = not post.published  # Inverse la valeur de 'published'
        post.save()
        return redirect('posts:home')