from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import RegistrationForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import UserAdditionalInfo
from .context_processors import user_additional_info
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage


# @login_required(login_url='/')
def Demo(request):
    return render(request, "pages/demo.html")


class RegistrationView(View):
    def get(self, request):
        if request.method == 'POST':
            return redirect('login')
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'pages/login/sign_up.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "User Creation Successful !!")
            return redirect('login')
        else:
            messages.error(request, "Something Went Wrong")
            return render(request, 'pages/login/sign_up.html', {'form': form})


@login_required(login_url='/')
def UserProfile(request, user):
    # userinfo = UserAdditionalInfo.objects.get(username=user)
    return render(request, "pages/user_profile.html")


@login_required(login_url='/')
def EditUserProfile(request, user_id, username):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        useradditional = UserAdditionalInfo.objects.get(username=username)
        useradditional.username = request.POST.get('username')
        useradditional.contact_no = request.POST.get('contact')
        useradditional.user_role = request.POST.get('user_role')
        useradditional.profession = request.POST.get('profession')
        useradditional.social_link = request.POST.get('social_link')
        if 'pro_pic' in request.FILES:
            useradditional.profile_picture = request.FILES['pro_pic']
        useradditional.save()
        messages.success(request, "User Profile Updated Successfully !")
        return redirect(reverse('user_profile', args=[user.username]))


@login_required(login_url='/')
def AddUserAdditionalInfo(request, user_id, user):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        additionalinfo = UserAdditionalInfo()
        additionalinfo.username = user
        additionalinfo.user_full_name = user
        additionalinfo.contact_no = request.POST.get('contact')
        additionalinfo.user_role = request.POST.get('user_role')
        additionalinfo.profession = request.POST.get('profession')
        additionalinfo.social_link = request.POST.get('social_link')
        if 'pro_pic' in request.FILES:
            additionalinfo.profile_picture = request.FILES['pro_pic']
        additionalinfo.save()
        messages.success(request, "User Additional Info Added Successfully !")
        return redirect(reverse('user_profile', args=[user.username]))

