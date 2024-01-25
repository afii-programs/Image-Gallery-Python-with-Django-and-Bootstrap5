from typing import Any
from django.contrib import messages
from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView, DetailView, FormView
from .models import Post
from .forms import PostForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['my_thing'] = 'Heyy this is the context...'
        context['posts'] = Post.objects.all().order_by("-id")

        return context
    
class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post

class AddPost(FormView):
    template_name = 'add_post.html'
    form_class = PostForm
    success_url = '/'


    def dispatch(self, request, *args: Any, **kwargs: Any):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    

    def form_valid(self, form):

        new_object = Post.objects.create(
            title = form.cleaned_data['text'],
            image = form.cleaned_data['image'],
        )

        messages.add_message(self.request,messages.SUCCESS,"Successfully Created! ")

        return super().form_valid(form)