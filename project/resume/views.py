from django.shortcuts import render
from .models import Resume,Post

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    resume = Resume.objects.get(pk=1)
    return render(request, 'about.html',{"resume":resume})

def blog(request):
    posts = Post.objects.all().order_by('-date')
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        posts = posts.filter(title__icontains = item_name)
    return render(request, 'blog.html',{"posts":posts})

#class postlistview(ListView):
#   model = Post
#    template_name = 'blog.html'
#   context_object_name = 'posts'
#    ordering = ['-date']
    