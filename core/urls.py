from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home_page_view, ticket_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('tickets/', include(('tickets.urls', 'tickets'), namespace='tickets')),
    path('profile/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('ticket/', ticket_view, name='ticket'),
    path('', home_page_view, name='home'),
    path('home/', home_page_view, name='landing'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)