from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from django.urls import reverse


# Create your views here.
def login_page(request):
    template = loader.get_template('login_page.html')

    return HttpResponse(template.render( {} , request))    

def user_authenticate(request):
        if request.method == 'POST' :
             email = request.POST.get('email')
             password = request.POST.get('password')

             user = authenticate(request , username=email , password=password)

             if user is not None:
                  login(request , user)

                  return redirect(reverse('dashboard') )
             
             else:
                   if not User.objects.filter(email=email).exists():
                    messages.error(request , 'The email address you entered is incorrect.')

                   else:
                    messages.error(request , 'The password you entered is incorrect.')

                   return render (request , 'login_page.html' , {'email': email } )


def signup(request):
      template = loader.get_template('signup.html')

      return HttpResponse(template.render({} , request))

def create_user(request):

     if request.method == 'POST':

          username = request.POST.get('username')
          email = request.POST.get('email')
          password = request.POST.get('password')

          if User.objects.filter(email=email).exists():
               messages.error(request , 'Email already in use.')
               return render(request, 'signup.html', {'username': username, 'email': email})
          
          if len(password) < 8 :
               messages.error(request , 'Password must have at least 8 characters.')
               return render(request, 'signup.html', {'username': username, 'email': email})

          else:

               user = User.objects.create_user(username = username , email = email , password = password)
               user.save()
               messages.success(request, 'Account created successfully. Please login.')

               return redirect(reverse('login_page') )


def dashboard(request):
     template = loader.get_template('dashboard.html')

     return HttpResponse(template.render({} , request))