from django.urls import path

from .views import ticket_home_view, ticket_detail_view, JitBitAPI, jitbit

urlpatterns = [
    path('', ticket_home_view, name='home'),
    path('<int:id>', ticket_detail_view, name='detail'),
    path('jitbit', jitbit, name='jitbit' )
]