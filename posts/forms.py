from crispy_forms.bootstrap import FormActions
from django import forms
from django.contrib.auth import authenticate
from posts.models import Publisher
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Hidden


class PostForm(forms.Form):
    name = forms.CharField(
        label='Post',
        max_length=50,
        required=True
    )
    link = forms.URLField(
        label='Link',
        max_length=200,
        initial='http://',
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            'name',
            'link',
            Submit('submit', 'Submit')
        )



class PublisherForm(forms.Form):
    firstname = forms.CharField(label = 'Firstname', max_length = 50, required = True)
    lastname = forms.CharField(label = 'Lastname', max_length = 50, required = True)
    login = forms.CharField(label = "Login")
    email = forms.EmailField(label = "Email")
    specialisation = forms.CharField(label = "Specialisation")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)
    password_bis = forms.CharField(label = "Password", widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super (PublisherForm, self).clean()
        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')
        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(PublisherForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            'firstname',
            'lastname',
            'login',
            'email',
            'specialisation',
            'password',
            'password_bis',
            Submit('submit', 'Submit')
        )

class LoginForm(forms.Form):
    username = forms.CharField(label="Login")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Wrong login or password")
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit', 'Submit')
        )