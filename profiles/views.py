from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm


def profile_edit_view(request):
    template = 'profile/profile-edit.html'
    profile = request.user.profile
    form = ProfileForm(request.POST or None, instance=profile)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('tickets:home')

    context = {
        'form': form
    }

    return render(request, template, context)

