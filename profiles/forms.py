from django import forms


from core.const import DIVISION_CHOICES
from .models import Profile

class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True

    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={'placeholder': 'First Name', 'autocomplete': 'first name'}
        )
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(
            attrs={'placeholder': 'Last Name', 'autocomplete': 'last name'}
        )
    )
    phone = forms.IntegerField(
        label='Phone',
        widget=forms.TextInput(
            attrs={'placeholder': 'Phone'}
        )
    )
    employee_number = forms.IntegerField(
        label='Employee Number',
        widget=forms.TextInput(
            attrs={'placeholder': 'Employee Number'}
        )
    )
    extension = forms.IntegerField(
        label='Extension',
        widget=forms.TextInput(
            attrs={'placeholder': 'Extension'}
        )
    )

    class Meta:
        model = Profile
        fields = '__all__'