
# ** we haven't actually mapped our url pattern to the view
# function above -> to do this we're going to create a new
# bot module in our blog directory called urls.py and in that
# file is where we'll map the urls that we want to correspond
# to each view function

from django.urls import path
from . import views
from . views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)


urlpatterns = [
    # -setting up the path for the homepage (class based list view)
    path('', PostListView.as_view(), name="blog-home"),
    # -setting up the path for the user's posts
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    # -setting up the path for the about page
    path('about/', views.about, name="blog-about"),
    # -setting up the path for the individual blog post
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    # -setting up the path for the create post form
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    # -setting up the path for the update post form
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    # -setting up the path for the delete post form
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
]
