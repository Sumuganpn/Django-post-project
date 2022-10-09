from django.core import paginator
from django.db import models
from django.shortcuts import render , get_object_or_404
from .models import post
from django.views.generic import (ListView , 
                                  DetailView , 
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import (LoginRequiredMixin, # for creating post login is required, see in class createview at bottom  
                                       UserPassesTestMixin) # used to detect not to update others post
from django.contrib.auth.models import User
#--------------------------------------------------------------------------------------
def sumugan(request):
    context = { 
        'posts' : post.objects.all(),  #FOR BEGINNING RENDER PROGRAM [homepage] 
    }                                  #LATER CHANGED TO POSTLISTVIEW AS HOME PAGE
    return  render(request , 'training/sumugan.html', context)
#--------------------------------------------------------------------------------------
class PostListView(ListView):
    model = post
    template_name  = 'training/sumugan.html' # goes to template
    context_object_name = 'posts' # goes to posts database and show all the content 
    
    ordering = ['-date_posted']  #'date_posted'  = old to new, 
                                 #'-date_posted' = new to old
   
    paginate_by = 4   # used to show how many post should been showed in one page 

#--------------------------------------------------------------------------------------                               
class UserPostListView(ListView):
    model = post
    template_name  = 'training/user_posts.html' # goes to template
    context_object_name = 'posts' # goes to posts database and show all the content 
    paginate_by = 4   # used to show how many post should been showed in one page

    def get_queryset(self):  # used to get the post of that username alone
        user =  get_object_or_404(User, username = self.kwargs.get('username'))
        return  post.objects.filter(author = user).order_by('-date_posted')

#--------------------------------------------------------------------------------------
class PostDetailView(DetailView):
    model = post 
    template_name = 'training/post_detail.html'

#-----------------------------------------------------------------------------------    
class PostCreateView(LoginRequiredMixin, CreateView): # for loginrequiredmixin 
    model = post                                      #   see up for definition
    fields = ['title','content']
    template_name = 'training/post_form.html'

    def form_valid(self, form):                  # function for loginrequiredmixin
        form.instance.author = self.request.user # create a post with logged in
        return super().form_valid(form)          # account as the author name  
    
#-------------------------------------------------------------------------------------- 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # for loginrequiredmixin see up for definition
    model = post                                                           # for UserPassesTestMixin see up for definition
    fields = ['title','content']
    template_name = 'training/post_form.html'

    def form_valid(self, form):                 # function for loginrequiredmixin
        form.instance.author = self.request.user # create a post with logged in
        return super().form_valid(form)          # account as the author name

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:  # function for userpassestestmixin 
            return True
        return False

#--------------------------------------------------------------------------------------
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post 
    success_url = '/'
    template_name = 'training/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:  # function for userpassestestmixin 
            return True
        return False

#--------------------------------------------------------------------------------------
def world(request):
    return render(request, 'training/world.html')

#--------------------------------------------------------------------------------------    

