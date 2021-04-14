from django.shortcuts import render

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