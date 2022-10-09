from django.urls import path
from . views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

# At bottom both postcreateview and postupdateview share same template post_form
# postdetailview = post_detail
# postdelectview = post_confirm_delect

urlpatterns = [
    path('', PostListView.as_view(), name='sumugan'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'), # <int:pk> is there because it should know which post(post_id) should be updated
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('world' , views.world , name='world')
]