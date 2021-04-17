"""
alopex-helpdesk - A Django powered support desk

(c) Copyright Alopex Technologies LLC
All Rights Reserved. See LICENSE for details.

models.py - Model definitions.
"""

from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _, ugettext
import mimetypes
import datetime
import re
import os
import uuid

from markdown import markdown
from markdown.extensions import Extension

from core import settings

def format_time_spent(time_spent):
    if time_spent:
        time_spent = "{0:02d}h:{1:02d}m".format(
            time_spent.seconds // 3600,
            time_spent.seconds // 60
        )
    else:
        time_spent = ""
    return time_spent

class EscapeHtml(Extension):
    def extend_markdown(self, md, md_globals):
        del md.preprocessors['html_block']
        del md.inlinePatterns['html']

def get_markdown(text):
    if not text:
        return ""
    return mark_safe(
        markdown(
            text,
            extensions=[
                EscapeHtml(), 'markdown.extensions.nl2br',
                'mardown.extensions.fenced_code'
            ]
        )
    )

class Container(models.Model):
    """
    A container is virutal standalone queue for tickets
    to allow for multiple departments to use autonomously
    """
    long_name = models.CharField(
        _('Long Name'),
        max_length=100,
    )
    short_name = models.CharField(
        _('Short Name'),
        max_length=50,
    )
    slug = models.SlugField(
        _('Slug'),
        max_length=50,
        unique=True,
    )
    email_address = models.EmailField(
        _('email Address'),
        blank=False,
        null=False,
    )
    new_ticket_cc = models.CharField(
        _('New Ticket CC Address'),
        blank=True,
        null=True,
        max_length=255,
    )
    updated_ticket_cc = models.CharField(
        _('Updated Ticket CC Address'),
        blank=True,
        null=True,
        max_length=255,
    )
    email_box = models.ForeignKey(
        'Email',
        on_delete=models.DO_NOTHING
    )
    dedicated_time = models.DurationField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.short_name}'

    class Meta:
        ordering = ('long_name'),
        verbose_name = _('Container')
        verbose_name_plural = _('Containers')

    @property
    def time_spent(self):
        total = datetime.timedelta(0)
        for val in self.ticket_set.all():
            if val.time_spent:
                total = total + val.time_spent
        return total
    

class Email(models.Model):
    user = models.CharField(
        _('Email Username'),
        max_length=200,
        blank=False,
        null=False,
    )
    password = models.CharField(
        _('Email Password'),
        max_length=30,
        blank=False,
        null=False,
    )
    email_type = models.CharField(
        _('Email Type'),
        max_length=5,
        choices=(('pop3', _('POP 3')), ('imap', _('IMAP'))),
        blank=False,
        null=False,
        default='imap'
    )
    host = models.CharField(
        _('Host Name'),
        max_length=30,
        blank=False,
        null=False,
    )
    port = models.IntegerField(
        _('Email Port'),
        blank=False,
        null=False,
        default=993
    )
    ssl = models.BooleanField(
        _('Use SSL'),
        blank=False,
        null=False,
        default=True
    )
    folder = models.CharField(
        _('Email Folder'),
        max_length=30,
        blank=False,
        null=False,
    )
    retrieval_interval = models.IntegerField(
        _('Email Check Interval'),
        blank=True,
        null=True,
        default='5',
    )
    last_check = models.DateTimeField(
        blank=True,
        null=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        if not self.folder:
            self.folder = 'INBOX'
        super(Email, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user}'


def mk_secret():
    return str(uuid.uuid4())


class Ticket(models.Model):

    NEW_STATUS = 0
    OPEN_STATUS = 1
    REOPENED_STATUS = 2
    RESOLVED_STATUS = 3
    CLOSED_STATUS = 4
    DUPLICATE_STATUS = 5

    STATUS_CHOICES = (
        (NEW_STATUS, _('New')),
        (OPEN_STATUS, _('Open')),
        (REOPENED_STATUS, _('Reopened')),
        (RESOLVED_STATUS, _('Resolved')),
        (CLOSED_STATUS, _('Closed')),
        (DUPLICATE_STATUS, _('Duplicate')),
    )

    PRIORITY_CHOICES = (
        (1, _('1. Critical')),
        (2, _('2. High')),
        (3, _('3. Normal')),
        (4, _('4. Low')),
        (5, _('5. Very Low')),
    )
    subject = models.CharField(
        _('Subject'),
        max_length=100,
    )
    issue = models.CharField(
        _('Issue'),
        max_length=200,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name=_('Category')
    )
    assocaited_employee = models.ForeignKey(
        'Employees',
        on_delete=models.CASCADE,
        verbose_name=_('Employees'),
        blank=True,
        null=True,
    )
    container = models.ForeignKey(
        'Container',
        on_delete=models.CASCADE,
        verbose_name=_('Container')
    )
    created = models.DateTimeField(
        _('Created'),
        blank=True,
        default=timezone.now()
    )
    modified = models.DateTimeField(
        _('Modified'),
        blank=True,
    )
    submitter = models.ForeignKey(
        get_user_model(),
        related_name=_('submitter'),
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    technician = models.ForeignKey(
        get_user_model(),
        related_name=_('technician'),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    status = models.IntegerField(
        _('Status'),
        choices=STATUS_CHOICES,
        default=NEW_STATUS
    )
    resolution = models.TextField(
        _('Resolution'),
        blank=True,
        null=True,
    )
    priority = models.IntegerField(
        _('Priority'),
        choices=PRIORITY_CHOICES,
        default=3,
        blank=3,
    )
    due_date = models.DateTimeField(
        _('Due on'),
        blank=True,
        null=True,
    )
    secret_key = models.CharField(
        _('Secret key'),
        max_length=36,
        default=mk_secret
    )
    master_ticket = models.ForeignKey(
        'Ticket',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    @property
    def time_spent(self):
        """
        Returns back the total time spent on a ticket
        """
        total = datetime.timedelta(0)
        for val in self.comment_set.all():
            if val.time_spent:
                total = total + val.time_spent
        return total

    def _get_assigned_to(self):
        """
        Return assigned to tech, unassigned in none
        """
        if not self.technician:
            return _('Unassigned')
        else:
            return f'{self.technician}'
    get_assigned_to = property(_get_assigned_to)

    def _get_ticket(self):
        return u'[%s]' % (self.container.slug, self.id)
    ticket = property(_get_ticket)

    def _get_ticket_for_url(self):
        return u"%s-%s" % (self.queue.slug, self.id)
    ticket_for_url = property(_get_ticket_for_url)

    def _get_status_css_class(self):
        if self.status == 0:
            return 'new'
        elif self.status == 1:
            return 'open'
        elif self.status == 4:
            return 'closed'
    get_status_css_class = property(_get_status_css_class)

    def _get_priority_css_class(self):
        if self.priority == 2:
            return "warning"
        elif self.priority == 1:
            return "danger"
        elif self.priority == 5:
            return "success"
        else:
            return ""
    get_priority_css_class = property(_get_priority_css_class)

    class Meta:
        get_latest_by = "created"
        ordering = ('id',)
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')

    def __str__(self):
        return '%s %s' % (self.id, self.issue)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('tickets:detail', kwargs={"id": self.id})

    def save(self, *args, **kwargs):
        if not self.priority:
            self.priority = 3
        self.modified = timezone.now()

        super(Ticket, self).save(*args, **kwargs)

    def get_markdown(self):
        return get_markdown(self.issue)

    @property
    def get_resolution_markdown(self):
        return get_markdown(self.resolution)


class Comment(models.Model):

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        verbose_name=_('Ticket'),
    )
    date = models.DateTimeField(
        _('Date'),
        default=timezone.now()
    )
    comment = models.TextField(
        _('Comment'),
        blank=True,
        null=True,
    )
    public = models.BooleanField(
        _('Tech Only'),
        blank=True,
        null=True,
        default=False,
    )
    user = models.ForeignKey(
        get_user_model(),
        related_name=_('commenter'),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    time_spent = models.DurationField(
        blank=True,
        null=True,
    )
    google_api = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )
    verizon_api = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )

    class Meta:
        ordering = ('-date',)
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return f'{self.comment}'

    def get_absolute_url(self):
        return u"%s#comments%s" % (self.ticket.get_absolute_url(), self.id)

    def save(self, *args, **kwargs):
        ticket = self.ticket
        ticket.modified = timezone.now()
        ticket.save()
        super(Comment, self).save(*args, **kwargs)

    def get_markdown(self):
        return get_markdown(self.comment)


class Attachment(models.Model):
    file = models.FileField(
        _('file'),
        upload_to='/',
        max_length=1000,
    )
    filename = models.CharField(
        _('Filename'),
        blank=True,
        max_length=1000,
    )
    mime_type = models.CharField(
        _('MIME Type'),
        blank=True,
        max_length=255,
    )
    size = models.IntegerField(
        _('Size'),
        blank=True,
    )
    def __str__(self):
        return f'{self.filename}'
    
    def save(self, *args, **kwargs):
        if not self.size:
            self.size = self.file.file.size
        if not self.filename:
            self.filename = f'{self.file}'
        if not self.mime_type:
            self.mime_type = \
                mimetpes.guess_type(self.filename, strict=False)[0] or \
                    'application/octet-stream'
        return super(Attachment, self).save(*args, **kwargs)

    class Meta:
        ordering = ('filename',)
        verbose_name = _('Attachment')
        verbose_name_plural = _('Attachments')
        abstract = True


class Category(models.Model):
    category = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    def __str__(self):
        return self.category


class Employees(models.Model):
    employee = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    def __str__(self):
        return self.employee


class Users(models.Model):
    user = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    def __str__(self):
        return self.user
