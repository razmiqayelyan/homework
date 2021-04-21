from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SnippetForm
from .models import Snippet
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.

def usblog(request):
	snipps = Snippet.objects.all()
	return render(request, 'indexg.html', {'snipps':snipps})

class PostDetailView(DetailView):
	model = Snippet
	template_name = 'detail.html'
	context_object_name = 'snipet'

class PostUpdateView(UpdateView):
	model = Snippet
	template_name = 'formka.html'
	form_class = SnippetForm
	context_object_name = 'snipet'

class PostDeleteView(DeleteView):
	model = Snippet
	success_url = '/'
	template_name = 'delete.html'
	context_object_name = 'snipet'









def snippet_detail(request):
	form = SnippetForm(request.POST or None,request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			form = SnippetForm
			messages.success(request, 'Successfully created')
			return redirect('usblog')
	return render(request, 'form.html', {'form':form})


def userpage(request, username):
	username = User.objects.get(username=username)
	snipps = Snippet.objects.all()
	return render(request, 'userpage.html', {'username':username,'snipps':snipps}) 

def profile(request, username):
	username = User.objects.get(username=username)
	snipps = Snippet.objects.all()
	return render(request, 'profile.html', {'username':username,'snipps':snipps}) 


	

