from django.urls import path

from .views import profile_edit_view

urlpatterns = [
    path('edit', profile_edit_view, name='edit')
]
