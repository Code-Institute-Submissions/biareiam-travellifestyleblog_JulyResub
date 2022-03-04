""" Libraries """
from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, category_view, category_list_view, AddCategoryView, like_view, AddCommentView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add-post"),
    path('add_category/', AddCategoryView.as_view(), name="add-category"),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cats>', category_view, name="category"),
    path('category-list/', category_list_view, name="category-list"),
    path('like/<int:pk>', like_view, name='like_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
