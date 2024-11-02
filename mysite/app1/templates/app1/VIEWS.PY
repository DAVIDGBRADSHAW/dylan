from django.shortcuts import render
def ruth(request):
    context = {
        'posts': posts
    }
    return render(request, 'app1/home.html', context)
  

posts = [
    {
        'author': 'ucs studentb1',
        'title':  'blll',
        'content': 'mmmmmm',
        'date_posted': 'june 01 , 2024'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/home.html', context)