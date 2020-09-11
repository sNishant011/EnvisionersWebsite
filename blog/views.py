from django.views import generic
from .models import Post
from Home.models import About


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'explanation.html'

    def get_context_data(self,  **kwargs):
        queryset = super().get_context_data(**kwargs)
        queryset['abouts'] = About.objects.all()
        queryset['title'] = 'Explanations | Envisioners'
        return queryset


class PostDetail(generic.DetailView):

    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self,  **kwargs):
        queryset = super().get_context_data(**kwargs)
        queryset['posts'] = Post.objects.all()
        queryset['abouts'] = About.objects.all()
        queryset['title'] = 'Explanations | Envisioners'
        return queryset
