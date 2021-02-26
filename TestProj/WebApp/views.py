from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FileUploadForm
from djangoconvertvdoctopdf.convertor import StreamingConvertedPdf
from .models import File
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def register_view(request):
    form = CreateUserForm()
    context = {'form': form}
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    return render(request, 'signup.html', context)


def login_view(request):
    if request.method == "POST":
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        user = authenticate(username=username1, password=password1)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully')
            return redirect('/docupload')
        else:
            messages.warning(request, 'Username or Password is Wrong')
    return render(request, 'login.html')


@login_required(login_url='login')
def custom_view(request):
    form = FileUploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/list')
    return render(request, 'fileupload.html', {'form': form})


@login_required(login_url='login')
def file_list(request):
    filelist = File.objects.all()
    return render(request, 'list.html', {'filelist': filelist})


@login_required(login_url='login')
def file_delete(request, pk):
    files = File.objects.get(id=pk)
    files.delete()
    return redirect('/list')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')
