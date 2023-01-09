from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views as app_views
urlpatterns = [
    # path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),

    path('', PostListView.as_view(), name="blog-home"),
    path('post-new/', PostCreateView.as_view(), name="blog-new"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="blog-update"),
    path('comment/<post_id>', views.comment, name='comment'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="blog-delete"),
    path('like/<post_id>', views.like, name='like'),
]
