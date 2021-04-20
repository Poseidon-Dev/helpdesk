from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from core.decorators import group_required

# @login_required
# @user_passes_test(lambda u: u.groups.filter(name='Technician').exists() | u.is_superuser)
def home_page_view(request):
    template = 'tickets/home.html'
    title = 'home'
    context = {
        'title': title,
    }
    return render(request, template, context)

def ticket_view(request):
    template = 'tickets/ticket.html'
    title = 'Ticket'
    context = {
        'title': title,
    }
    return render(request, template, context)