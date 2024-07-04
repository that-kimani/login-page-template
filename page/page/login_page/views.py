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
                   messages.error(request , 'Incorrect email or password')
                   return redirect(reverse('login_page'))



def dashboard(request):
     template = loader.get_template('dashboard.html')

     return HttpResponse(template.render({} , request))

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

          else:

               user = User.objects.create_user(username = username , email = email , password = password)
               user.save()

               return redirect(reverse('login_page') )

     
     

     
     
