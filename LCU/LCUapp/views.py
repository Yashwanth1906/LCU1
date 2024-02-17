
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def showmain(r):
    return render(r,'main.html')
def showmovie(r):
    return render(r,'movie.html')
def showchr(r):
    return render(r,'char.html')
def showgames(r):
    return render(r,'games.html')
def showbooks(r):
    return render(r,'books.html')
def shownews(r):
    return render(r,'news.html')
def showsignup(r):
        if r.method == "POST":
            x= r.POST.get('firstname')
            y= r.POST.get('lastname')
            z= r.POST.get('username')
            a= r.POST.get('email')
            b= r.POST.get('password')
            c= r.POST.get('cpassword')

            myuser = User.objects.create_user(z,a,b)
            myuser.first_name=x
            myuser.last_name=y
            print(myuser)
            myuser.save()

            messages.success(r,"Your account has been successfully created")

            return redirect('/login')
        return render(r,'signup.html')
def showlogin(r):
    if r.method == "POST":
        user1 = r.POST['username']
        pass1 = r.POST['password']

        user = authenticate(username=user1,password=pass1)

        if user is not None:
            login(r, user)
            fname = user.first_name
            return render(r,'main.html',{'fname':fname})
        else:
            messages.error(r,"Bad Informations!")
            return redirect('/signup')
    return render(r,'login.html')