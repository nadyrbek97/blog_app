from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

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

def about(request):
    return render(request, 'blog/about.html', { 'title' : 'About'})
    #return HttpResponse("<h1>ABOUT PAGE</h1>")




# Where we have to put our templates in specific application
# blog -> templates -> blog -> template.html
