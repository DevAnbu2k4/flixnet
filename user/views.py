from django.shortcuts import render, redirect
from . models import single, group
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    all_video = single.objects.all()
    all_group = group.objects.all()
    return render(request, 'user/index.html',{'all_video':all_video, 'all_group':all_group})

def search_item(request):
    if request.method == 'POST':
        query_name = request.POST.get('name', None)
        if query_name:
            results = single.objects.filter(name__icontains=query_name)
            return render(request, 'user/result.html', {'results':results})

    return render(request, 'user/index.html')

def signup(request):
    if request.method=='POST':
       username = request.POST['username']
       email = request.POST['email']
       password1= request.POST['password']
       password2 = request.POST['password2']
    
       if password1 == password2:
           if User.objects.filter(username=username).exists():
               messages.info(request, 'Username taken')
               return redirect('signup')
           elif User.objects.filter(email=email).exists():
               messages.info(request, 'Email taken')
               return redirect('signup')
           else:   
                user = User.objects.create_user(username=username, email=email,password=password1)
                user.save();
                messages.info(request, 'User created')

       else:
           messages.info(request, 'Password not matching')
           return redirect('signup')
       return redirect('signin')
    return render(request, 'user/signup.html')


def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'invalid email or password')

    return render(request, 'user/signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def dynamic(request, pk):
    obb = single.objects.get(name=pk)
    oss = group.objects.get(singles=obb)
    return render (request, 'user/video.html', {'obb':obb, 'oss':oss}) 

def groupdyn(request, pk):
    obj = group.objects.get(title=pk)
    return render (request, 'user/dynamic.html', {'obj':obj})