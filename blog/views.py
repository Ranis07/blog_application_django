import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post, About_descript
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#importing classbasedview
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


#This is class-based view
class PostListView(ListView):
	model = Post
	'''by default the template is called like this: <app>/<model>_<view_type> so in this case,
	it's called like blog/post_list. Since we donot have that path created for out template, we are
	specifying our own template in template_name variable'''
	template_name = 'blog/home.html'  
	context_object_name = 'posts' #by default the variable name is called object but we have set 'posts' here
	ordering = ['-date_posted']
	paginate_by = 5


class UserPostListView(LoginRequiredMixin,ListView):
	model = Post
	template_name = 'blog/user_posts.html'  
	context_object_name = 'posts'
	paginate_by = 5

	#To get username from the url we use get_queryset()
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username')) #here kwargs is query param. And Query parameters are a defined set of parameters attached to the end of a url.
		return Post.objects.filter(author=user).order_by('-date_posted')


'''Here we are trying to specify name of template and context as recommended by django i.e. 
using default template and contextname. Remember: default template is: <app>/<model>_<view_type>
and default context_object_name is object'''
class PostDetailView(DetailView):
	model = Post #Post is from from models.py

#LoginRequired decorators cannot be used in class, so loginrequiredmixin have been used
class PostCreateView(LoginRequiredMixin,CreateView):
	'''here its default template is <app>/<model>_form.html'''
	model = Post
	fields = ['title', 'content'] #fields is required since this createview will also be associated with forms
	
	'''this function is created to assign the user when creating a post'''
	def form_valid(self, form):
		form.instance.author = self.request.user #author instance of the form = current logged in user
		return super().form_valid(form) #since by creating we override parent class, its better to return .form_valid() of parent class again after specifying the user


'''UserPassesTestMixin is mixin that allows only authentic user can only update his/her post. So the
user has to pass certain test before updating the post that is test_func() method.'''
'''And for this updateview, default template is also post_form.html'''
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self): #this method should be named test_func
		post = self.get_object() #getting object of the post to get the author of the post
		if self.request.user == post.author: #if loggedin user = selected post author
			return True
		return False

'''for deleteview, default template is <appname>/<modelname>_confirm_delete'''
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url = '/' #success url directs, after deleting post where should it be redirected to. And by '/' means to homepage.

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False



#This is function-based view
def about(request): 
	return render(request, 'blog/about.html', context={'posts_about':About_descript.objects.all(), 'title':'About'})


def contact(request):
	if request.method == 'POST':
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			subject = contact_form.cleaned_data['subject']
			message = contact_form.cleaned_data['message']
			sender = contact_form.cleaned_data['sender']
			cc_myself = contact_form.cleaned_data['cc_myself']

			recipients = [os.environ.get('EMAIL_USER')]
			if cc_myself:
				recipients.append(sender)

			send_mail(subject,message,sender,recipients)
			return redirect('contact_success')
	else:
		contact_form = ContactForm()

	context = {'contact_form':contact_form,'title':'Contact'}
	return render(request,'blog/contact.html',context)
	
def contact_success(request):
	return render(request,'blog/contact_success.html',{'title':'Contact'})
