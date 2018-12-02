from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# posts = [
#     {
#         'author' : 'Nadyrbek',
#         'title' : 'Blog 1',
#         'content' : 'This is contect of blog 1',
#         'date_posted' : 'November 30, 2018'
#     },
#     {
#         'author' : 'Ajara',
#         'title' : 'Blog 2',
#         'content' : 'This is contect of blog 2',
#         'date_posted' : 'December 1, 2018'
#     }
# ]


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    #return HttpResponse("<h1>HOME<h1>")


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #ListView will looping over Object List istead Post.objects.all()
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

#LoginRequiredMixin is saying us that we have to login before create a blog
#as we do it in fnc_based view with @login_required decorator
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # because post must have an author
        form.instance.author = self.request.user
        # this line run def in our parrent class
        return super().form_valid(form)

#UserPassesTestMixin is check if is the owner of post or not
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # because post must have an author
        form.instance.author = self.request.user
        # this line run def in our parrent class
        return super().form_valid(form)

    #we can create this method
    #UserPassesTestMixin will test user pass certain test conditions
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    #we need success_url to redirect after deleting
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', { 'title' : 'About'})
    #return HttpResponse("<h1>ABOUT PAGE</h1>")




# Where we have to put our templates in specific application
# blog -> templates -> blog -> template.html
