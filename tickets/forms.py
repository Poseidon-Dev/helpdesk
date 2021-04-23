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
        widget=forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Ticket Detail'}),
        required=False,
        label='Detail',
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        label='Category',
        widget=forms.Select(attrs={'class': 'select'})
    )
    associated_employee = forms.ModelChoiceField(
        queryset=Employees.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'select hidden'})
    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        required=True,
        label='Sub Category',
        widget=forms.Select(attrs={'class': 'select'})
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
        self.fields['category'].empty_label = "Select Category..."
        self.fields['subcategory'].empty_label = "Select Sub Category..."
        self.fields['associated_employee'].empty_label = "Select Employee..."

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id).order_by('subcategory')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set.order_by('subcategory')

        if 'associated_employee' in self.data:
            try:
                associated_employee = int(self.data.get('associated_employee'))
            except (ValueError, TypeError):
                pass

    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ('container', 'subject', 'created', 'modified', 'submitter', 'technician', 'division', 'status', 'resolution', 'priority', 'due_date', 'secret_key', 'master_ticket')
