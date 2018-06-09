from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  Comment
from .models import  post
from .forms import CommentForm
from django.contrib.auth import authenticate, login


# def index(request):
#     return HttpResponse('i love coding because coding makes me happy')


def sign(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = Comment(name = request.POST['name'], comment = request.POST['comment'])
			new_comment.save()
			return redirect('index2')
	else:
		form = CommentForm()
	context = {'form': form}
	return render(request, 'post/form.html', context)
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user. 
            return render(request, 'post/succes.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'post/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'post/login.html')



def index(request):
    posts = post.objects.all()[:10]
    mypost_ = {'posts': posts}
    return render(request, 'post/index.html', mypost_)
        
def second(request):
    comments = Comment.objects.order_by('-date_added')
    context = {'comments': comments}
    return render(request, 'post/index2.html', context )
    