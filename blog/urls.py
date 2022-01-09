from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
	#PostListView is a class-based view and .as_view() converts it into a real view.
    path('', PostListView.as_view(), name='blog-home'), 
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'), 

	#here 'int:' makes sure that url is resulted in integer, like (localhost:post/1) and the-
	#-word pk is primarykey, django recommends like this to pass id of a post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), 

    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), 
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]