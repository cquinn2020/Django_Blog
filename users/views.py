from django.shortcuts import render, redirect
# messages are used to display messages to the user
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# create register view
def register(request):
    # if request has data -> create form with the data
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # save the user to the database
            form.save()
            username = form.cleaned_data.get('username')
            # send flash message to user
            messages.success(
                request, f"Your account has been created! You are now able to log in.")
            return redirect('login')
    else:  # any other request it instantiates an empty form
        form = UserRegisterForm()
    # last arg is the context
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    # if request has data -> create form with the data
    if request.method == 'POST':
        # instantiate empty forms for the profile and update forms
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        # if the forms are valid -> save the data to the database
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # send flash message to user
            messages.success(
                request, f"Your account has been updated!")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    # - pass into the template by passing the context (create a dictionary)
    # - the dictionary will be passed into the template and keys will be
    # the variable names in the template
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile.html', context)
