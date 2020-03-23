from django.shortcuts import render
from quiz.models import Post
from django.views.generic import ListView
# Create your views here.

def index(request):
    content = {
        'title': 'Home',
        'doc':  Post.objects.all()#.order_by('-date_posted')
    }
    return render(request, 'pages/index.html', content)

# List View Index
class HomeListView(ListView):
    model = Post
    # <app>/<model>_<viewtype>.html
    template_name = 'pages/index.html'
    context_object_name = 'doc'
    paginate_by = 3