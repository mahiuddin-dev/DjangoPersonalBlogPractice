# from django.http import request
from django.views.generic import  ListView
from django.views.generic.detail import DetailView
from .forms import CommentForm
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import redirect
from .models import Blogpost


class HomeView(ListView):
    template_name = "index.html"
    paginate_by = 6
    queryset = Blogpost.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            slug = Blogpost.objects.values('slug')[0]['slug']
            context['slug'] = slug
            return context
        except Exception:
            context['slug'] = ''
            return context


class BlogView(DetailView):
    model = Blogpost
    template_name = "blog-single-alt.html"

    def get_post(self):
        slug =  self.kwargs.get('slug')
        post = Blogpost.objects.get(slug=slug)
        post.read += 1
        post.save(update_fields = ['read'])
        return post

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['post'] = self.get_post()
        context['comments'] = self.get_post().comments.all()
        return context
    
    def post(self,request,slug):
        post = Blogpost.objects.get(slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)          
            new_comment.post = post            
            new_comment.save()
         
            # redirect to a new URL:           
            messages.success(request, 'Your comment submitted.')
            # return HttpResponse("Comment done")
            postlink = "/blog/"+post.slug
            return redirect(postlink)
        else:       
            form = CommentForm()


class SearchView(ListView):
    template_name = 'search.html'
    model = Blogpost

    def get(self,request,*args,**kwargs):
        term =  request.GET.get('q','')
        if len(term) > 0:
            self.results = self.model.objects.filter(Q(postTitle__icontains=term) | Q(description__icontains=term))
            return super().get(request,*args,**kwargs)
        else:
            self.results = ''
            return super().get(request,*args,**kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results'] = self.results
        context['queryset'] = self.results
        return context

    # def get(self, request):
    #     query = request.GET['q']
    #     print(query)
    #     return HttpResponse('Result') 'queryset': queryset,



