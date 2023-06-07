from django.views.generic import ListView, DetailView
from django.db.models import F, Q

from .models import Post, Tag, Category
from ..comments.models import Comment


class HomeListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My Blog'
        return context


class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/tags.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get(self, *args, **kwargs):
        object = self.get_object()
        object.views = F('views') + 1
        object.save()
        object.refresh_from_db()
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['comments'] = Comment.objects.filter(post=self.object)
        return context


class PostByCategoryListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class SearchListView(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        s = self.request.GET['s']
        return Post.objects.filter(Q(title__icontains=s) | Q(content__icontains=s))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f's={self.request.GET["s"]}&'
        return context
