from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

from .models import Ticket, Category, Comment, Employees, Container, SubCategory
from profiles.models import Profile

User = get_user_model()

class TicketForm(forms.ModelForm):

    # container = forms.ModelChoiceField(
    #     queryset=Container.objects.all(),
    #     required=True,
    #     label='Container',
    #     widget=forms.Select(attrs={'class': 'someselect'})
    # )
    # subject = forms.CharField(
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(attrs={'class': 'someinput'}),
    #     label='Subject',
    # )
    issue = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'textarea'}),
        required=True,
        label='Detail',
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        label='Category',
        widget=forms.Select(attrs={'class': 'someselect'})
    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        required=True,
        label='Sub Category',
        widget=forms.Select(attrs={'class': 'someselect'})
    )
    # submitter = forms.ModelChoiceField(
    #     queryset=User.objects.all(),
    #     required=False,
    #     label='Submitter',
    #     widget=forms.Select(attrs={'class': 'someselect'})
    # )  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategory'].queryset=SubCategory.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id).order_by('subcategory')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set.order_by('subcategory')

    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ('assocaited_employee', 'container', 'subject', 'created', 'modified', 'submitter', 'technician', 'division', 'status', 'resolution', 'priority', 'due_date', 'secret_key', 'master_ticket')
