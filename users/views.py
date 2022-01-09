from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			# afther submission of form, the data of form are stored cleaned_data, that's why we are accessing username through get()
			# and .cleaned_data only works if the form is valid.
			username = form.cleaned_data.get('username') 
			messages.success(request, f'Thank you for joining {username}, please login now.')
			return redirect('users-login')
	else:
		form = UserRegisterForm()

	context = {'form':form, 'title':'Register'}
	return render(request, 'users/register.html', context)

@login_required
def profile(request):
	if request.method == 'POST': 
		u_form = UserUpdateForm(request.POST,instance=request.user) #instance allows to fill the fields of the form with current user logged in 
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile) #we will be getting additional 'FILE data' for profile pic so adding request.FILES
		if u_form and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f"Your account has been successfully updated.")
			return redirect('users-profile')
	else:
		u_form = UserUpdateForm(instance=request.user) 
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {'u_form': u_form, 'p_form': p_form, 'title':'Profile'}
	return render(request,'users/profile.html', context)