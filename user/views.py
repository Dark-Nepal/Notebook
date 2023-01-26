from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required




def signup(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name =first_name, last_name=last_name,username=username,email=email,password=password)
            user.phone = phone
            user.is_active = True
            user.save()
            

#
            messages.success(request, 'Registration sucessfully')
            return redirect('signin')


    else:
        form = RegistrationForm()
        
    context = {
        'form' : form,
       
    }

    

    return render(request, 'user/register.html',context)


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'You are now logged in.')
            return redirect('entry')
        else:
            messages.error(request, 'Invalid login credential')
            return redirect('signin')
    return render(request, 'user/login.html')

@login_required(login_url = 'signin')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are loged out.')
    return redirect('entry')
