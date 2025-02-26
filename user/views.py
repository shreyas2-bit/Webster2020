from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileCreateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from .models import Profile
from Post.models import Post
from Post.views import PostListView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse


# Create your views here.
def register(request):
	if(request.method == 'POST'):
		form1 = UserRegisterForm(request.POST)
		if(form1.is_valid()):
			form1.save()
			username = form1.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}! You can now log in')
			return redirect('login')
	else:
		form1 = UserRegisterForm()
		form2 = ProfileCreateForm()
	context = {
		'form1': form1,
	}
	return render(request, 'users/register.html', context)

@login_required
def profile(request,slug):
	userd = User.objects.filter(username__iexact=slug).first()
	if request.user.is_authenticated:
		if(request.method == 'POST'):
			p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
			if(p_form.is_valid()):
				p_form.save()
				messages.success(request, 'Account has been updated.')
				return redirect('profile',slug=slug)
		else:
			p_form = ProfileUpdateForm(instance = request.user.profile)

		context = {
		'pform':p_form,
		'userd':userd,
		'slug':slug
		}
	else:
		context = {
		'userd':userd,#instance of current user
		'slug':slug
		}
	context['posts'] = Post.objects.filter(author__username = slug,grouppost__isnull=True)#getting post which user made publicily
	
	following= userd.profile.followings.all()
	context['following']=following
	follower = userd.profile.followers.all()
	context['followers'] = follower

	return render(request, 'users/profile.html', context)

@login_required
def notification(request):
	context={}
	# print(datetime.now())
	# print(request.user.profile.notif)
	context['posts'] = Post.objects.filter(date_posted__gte=request.user.profile.notif, grouppost__isnull=True)
	request.user.profile.notif=timezone.now()
	request.user.profile.save()
	return render(request,'users/notifications.html', context)

def test(request):
	context={}
	follows_users = request.user.profile.followings.all()
	post = Post.objects.filter(author_id__in=follows_users)
	context['post']=post
	return render(request,'users/test.html',context)

def following(request,user):
	user=User.objects.filter(username=user).first()
	context={}
	following= user.profile.followings.all()
	context['following']=following
	return render(request,'users/following.html',context)

def followers(request,user):
	context = {}
	user = User.objects.filter(username=user).first()
	follower = user.profile.followers.all()
	context['followers'] = follower
	return render(request, 'users/followers.html', context)

@login_required
def follow(request,user):
	if(request.method == 'POST'):
		user=User.objects.filter(username=user).first()
		user.profile.followers.add(request.user)
		request.user.profile.followings.add(user)
	return JsonResponse({'success':"success"})

		
@login_required
def unfollow(request,user):
	if(request.method == 'POST'):
		user=User.objects.filter(username=user).first()
		user.profile.followers.remove(request.user)
		request.user.profile.followings.add(user)
	return JsonResponse({'success':"success"})
		
	