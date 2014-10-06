from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

# Create your views here.
from posts.forms import PostForm, PublisherForm, LoginForm
from posts.models import Post, Publisher


def index(request):
    latest_post_list = Post.objects.all().order_by('-date_pub')[:5]
    context = {
        'latest_post_list': latest_post_list
    }
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'posts/detail.html', {'post': post})

@login_required
def get_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # process data in form.cleaned_data
            name = form.cleaned_data['name']
            link = form.cleaned_data['link']

            p = Post(name=name, link=link, publisher_id=request.user.id)
            p.save();

            #redirect
            return HttpResponseRedirect('/posts')

    else:
        form = PostForm()

    return render(request, 'posts/post.html', {'form': form})

@login_required
def get_publisher(request):
    if request.POST:
        form = PublisherForm(request.POST)
        if form.is_valid():
            # process data in form.cleaned_data
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            specialisation = form.cleaned_data['specialisation']

            new_user = User.objects.create_user(username=login, email=email, password=password)
            new_user.isActive = True
            new_user.first_name = firstname
            new_user.last_name = lastname
            new_user.save()

            new_publisher = Publisher(user_auth=new_user, specialisation=specialisation)
            new_publisher.save()

            #redirect
            return HttpResponseRedirect('/posts')
        else:
            render(request, 'posts/publisher.html', {'form': form})

    else:
        form = PublisherForm()
    form = PublisherForm()
    return render(request, 'posts/publisher.html', {'form': form})


def connection(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET['next'])
        return render(request, 'posts/connection.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'posts/connection.html', {'form': form})

@login_required
def log_out(request):
    logout(request)
    return render(request, 'posts/index.html')
