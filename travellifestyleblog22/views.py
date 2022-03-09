""" Libraries """
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.contrib import messages


def my_posts(request):
    """ Create my posts page """
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user.id)
        return render(request,"my_posts.html", {
            "posts" : posts
        })

    else:
        messages.success(request, ("You are not authorized to view this page"))
        return redirect('home')



def like_view(request, pk):
    """ Function which will allow user to like and deslike post """
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


def category_view(request, cats):
    """ Function which will allow users to sort the posts into categories """
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'category.html', {'cats': cats.title(), 'category_posts': category_posts})


def category_list_view(request):
    """ Function which will allow user to see the post sorted by category """
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


class AddCategoryView(CreateView):
    """ It will allow users to add new categories """
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class HomeView(ListView):
    """ Allow user to see the home page and the posts on it  """
    model = Post
    template_name = 'home.html'
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArticleDetailView(DetailView):
    """ Thies will allow users to see each post individually """
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        engagement = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = engagement.total_likes()

        liked = False
        if engagement.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    """ This will allow users to add posts """
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class UpdatePostView(UpdateView):
    """ This will allow user to update their own posts """
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class DeletePostView(DeleteView):
    """ This will allow users to delete their own posts """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddCommentView(CreateView):
    """ This will allow users to add comments """
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


