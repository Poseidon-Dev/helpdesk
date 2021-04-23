from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
import json, os, requests
from requests.auth import HTTPBasicAuth

from .models import Ticket, Category, Users, Container, Comment, SubCategory
from .forms import TicketForm

def ticket_home_view(request):
    template = 'tickets/home.html'
    title = 'Home'
    tickets = Ticket.objects.all()
    context = {
        'title': title,
        'tickets': tickets
    }
    return render(request, template, context)

def ticket_create_view(request):
    template = 'tickets/new.html'
    title='Create Ticket'
    container = Container.objects.get(id=1)
    
    form = TicketForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance = Ticket(
            container=container,
            issue=form.cleaned_data['issue'],
            category=form.cleaned_data['category'],
            subcategory=form.cleaned_data['subcategory'],
            associated_employee=form.cleaned_data['associated_employee'],
            created=timezone.now(),
            status=Ticket.NEW_STATUS,
            submitter=request.user,
            priority=3,
        )
        instance.save()
        return redirect('tickets:home')

    context = {
        'title': title,
        'form' : form,
    }

    return render(request, template, context)

def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = SubCategory.objects.filter(category_id=category_id).order_by('subcategory')
    return render(request, 'tickets/subcategory_dl_list.html', {'subcategories': subcategories})


def ticket_detail_view(request, id):
    template = 'tickets/ticket.html'
    ticket = Ticket.objects.get(id=id)
    comments = Comment.objects.filter(ticket=ticket)
    title = ticket.id

    context = {
        'title': title,
        'ticket': ticket,
        'comments': comments,
    }
    return render(request, template, context)

class JitBitAPI:

    def __init__(self):
        self.auth = HTTPBasicAuth(settings.HELPDESK_USER, settings.HELPDESK_PWD)

        if not self.test_creds():
            raise ValueError("Authorization failed, please check your credentials")
        else:
            print('Connection to Arizona Pipeline JitBit Established')

    def test_creds(self):
        """
        Ensure a connection to the JitBit API
        """
        response = self._make_request("Authorization")
        return response.status_code == 200

    def _make_request(self, method):
        """
        Default method for JitBit API calls
        """
        url = f'{settings.HELPDESK_URL}/api/{method}'
        print(url)
        return requests.get(url, auth=self.auth)

    def pull_tickets(self):
        """
        Retrieves all unclosed tickets from JitBit API
        """
        method = 'Tickets/?mode=unclosed&count=50'
        response = self._make_request(method)
        tickets = json.loads(response.content)
        return tickets

    def push_tickets(self, tickets=None):
        """
        Pushes pulled tickets into tickets db
        """
        pass

    def pull_comment(self, ticket):
        """
        Pull comments for a select ticket
        """
        method = f'comments?id={ticket}'
        response = self._make_request(method)
        comments = json.loads(response.content)
        return comments

    def push_comments(self):
        """
        Batch process push_comments to populate local db with all available tickets
        """
        pass

def jitbit(request):
    tickets = JitBitAPI().pull_tickets()
    return JsonResponse(tickets, safe=False)