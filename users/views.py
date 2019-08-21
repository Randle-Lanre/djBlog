from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
#the redirect was imported and used so that when the user registers
#he does return back to the same form, instead we redirect the user to,
#the home page or any other page

def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()#saves the user else doesn't
			username=form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! you are now able to login')
			return redirect('login')
	else:
		form= UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
	if request.method == 'POST':
	#instantiate class of the userupdate form
		u_form= UserUpdateForm(request.POST, instance=request.user)#populate the form
		#instantiate class of the profileupdateform
		p_form= ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)#populate the form with profile data
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form= UserUpdateForm(instance=request.user)#populate the form
		#instantiate class of the profileupdateform
		p_form= ProfileUpdateForm(instance=request.user.profile)#populate the form with profile data
	#now pass it to the template, using context
	context={
		'u_form':u_form,
		'p_form':p_form
	}

	return render (request, 'users/profile.html', context)

# types of messages(messages not message),
# there are 
# message.info
# message.debug
# message.warning
# message.error
#message.success