from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm

# Create your views here.


def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            un = form.cleaned_data.get('username') # pylint: disable=invalid-name
            messages.success(request, f'Account created for {un}.')
            return redirect('sign_in')

    elif request.method == "GET":
        form = UserSignUpForm()

    return render(request, 'users/signup.html', {'form': form})
