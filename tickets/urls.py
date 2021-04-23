from django.urls import path

from .views import ticket_home_view, ticket_detail_view, JitBitAPI, jitbit, ticket_create_view, load_subcategories

urlpatterns = [
    path('', ticket_home_view, name='home'),
    path('new', ticket_create_view, name='new'),
    path('ajax/load-subcategories', load_subcategories, name='ajax_load_subcategories' ),
    path('<int:id>', ticket_detail_view, name='detail'),
    path('jitbit', jitbit, name='jitbit')
]