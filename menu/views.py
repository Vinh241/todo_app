from django.views.generic import TemplateView,DetailView,DeleteView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TodoApp
from django.shortcuts import render

class HomePage(TemplateView):
    template_name= 'menu/homepage.html'
    http_method_names = ['get']
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = TodoApp.objects.all().order_by('time')
        context['posts'] = posts 
        return context
    
class PostDetailView(DetailView):
    template_name = 'menu/detail.html'
    http_method_names = ['get']
    model = TodoApp
    context_object_name = 'post'
class CreateNewPost(LoginRequiredMixin,CreateView):
    template_name='menu/create.html'    
    success_url='/'
    model = TodoApp
    fields = ['title','text','time']
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)
    def post(self,request,*args,**kwargs):
        post = TodoApp.objects.create(
            title = request.POST.get('title'),
            text = request.POST.get('text'),
            time = request.POST.get('time'),
            author = request.user,
        )
        return render(
            request,
            "include/post.html",
            {
            'post':post
            },
            content_type ="application/html"
        )
class deleteItem(DeleteView):
    template_name = 'menu/delete.html'
    model = TodoApp
    success_url = '/'
class updateItem(UpdateView):
    model = TodoApp
    template_name = 'menu/update.html'
    success_url= '/'
    fields= ['title','text','time']