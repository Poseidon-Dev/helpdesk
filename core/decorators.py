from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import render, reverse, redirect


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(u):
        if u.is_authenticated():
            groups = [group for group in groups]
            if set(group_names).symmetric_difference(groups) | u.is_superuser:
                return True
            return False
        return user_passes_test(in_groups)


def profile_required(view_func=None):
    """
    Decorator for views that checks if the user has configured their profile
    Redirecting them to their profile page if incomplete
    """
    def wrap(request, *args, **kwargs):
        try:
            profile = request.user.profile
        except ObjectDoesNotExist:
            return render(request, 'account/logout.html')

        if (not profile.first_name 
            or not profile.last_name
            or (profile.division == 98 or profile.division == None)
            or not profile.employee_number):
            return redirect('profiles:edit')
        else:
           return redirect('tickets:home')
    return wrap
