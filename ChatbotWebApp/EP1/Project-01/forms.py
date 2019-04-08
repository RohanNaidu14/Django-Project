from django import forms
from Project01.models import Post, Ticket
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class HomeForm(forms.Form):
    hello = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 1,
                "cols": 100,
                "placeholder": 'Type here to chat',
            }
        )
    )
    # text = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Type Here"}))


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

        )


# read more about this save function in detail
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )


Priority_Choices = [
    ('critical', 'Critical'),
    ('high', 'High'),
    ('low', 'Low'),
    ('very low', 'Very Low'),
]

Queue_Choices = [
    ('product queue', 'Product Queue'),
    ('network queue', 'Network Queue'),
    ('software queue', 'Software Queue'),
]


class TicketForm(forms.Form):
    queue = forms.CharField(
        label="Queue",
        widget=forms.Select(choices=Queue_Choices)
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "rows": 10,
            "cols": 50,
        }
        )
    )
    priority = forms.CharField(
        label="Priority",
        widget=forms.Select(choices=Priority_Choices)
    )
    email = forms.EmailField(required=True)
