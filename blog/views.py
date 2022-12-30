from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# logic for how we want to handle when a user
# goes to our blog homepage
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# class based view for the blog homepage
class PostListView(ListView):
    # model tells list view what model to query to create list
    model = Post
    # template_name tells list view what template to use to render the list
    template_name = 'blog/home.html'
    # context_object_name tells list view what to call the list in the template
    context_object_name = 'posts'
    # ordering tells list view how to order the list
    ordering = ['-datePosted']
    # paginate_by tells list view how many items to display per page
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    # override the get_queryset method to filter the posts by the user
    def get_queryset(self):
        # get the user
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # return the posts by the user
        return Post.objects.filter(author=user).order_by('-datePosted')


# class based view for individual blog posts
# will be looking for template with pattern <app>/<model>_<viewtype>.html -> blog/post_detail.html
class PostDetailView(DetailView):
    model = Post


# creating a Create View for our blog posts
# - will be a class based view and will inherit from CreateView class (form)
#  - will be looking for template with pattern <app>/<model>_<viewtype>.html -> blog/post_form.html
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields tells CreateView what fields to include in the form
    fields = ['title', 'content']

    # override the form_valid method to add author to the form data
    def form_valid(self, form):
        # add the author to the form data
        form.instance.author = self.request.user
        # call the super class form_valid method
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # fields tells CreateView what fields to include in the form
    fields = ['title', 'content']

    # override the form_valid method to add author to the form data
    def form_valid(self, form):
        # add the author to the form data
        form.instance.author = self.request.user
        # call the super class form_valid method
        return super().form_valid(form)

    # override the test_func method to check if the user is the author of the post
    def test_func(self):
        # get the post
        post = self.get_object()
        # check if the user is the author of the post
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # success_url tells DeleteView where to redirect to after a successful delete (we want to redirect to the homepage)
    success_url = '/'

    # override the test_func method to check if the user is the author of the post
    def test_func(self):
        # get the post
        post = self.get_object()
        # check if the user is the author of the post
        if self.request.user == post.author:
            return True
        return False


# about page logic
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
