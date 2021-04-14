from django.contrib import admin

from .models import Category, Ticket, Container, Comment, Users, Attachment, Employees, Email

admin.site.register(Ticket)
admin.site.register(Category)
admin.site.register(Users)
admin.site.register(Employees)
admin.site.register(Comment)
admin.site.register(Container)
admin.site.register(Email)
