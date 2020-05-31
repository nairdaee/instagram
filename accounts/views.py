from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout #function for loging in/out the user


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #saving user
            login(request, user) 
            
            return redirect("home")
    else:

        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user() # retrieves the user that is logging in
            login(request, user) #loges user in if form is valid
            if 'next' in request.POST:
                return redirect(request.POST.get('next')) #get the value that accompanied the request and redirects to that value
            else:                                #next is the name if the input type btw
              return redirect("home")
    else:

        form = AuthenticationForm()
    return render(request,'accounts/login.html',{"form":form})

def logout_view(request):
    if request.method == 'POST':
       logout(request) #will log current user out,no need to specify
       return redirect("home") #articles is the app name;list is the url name
