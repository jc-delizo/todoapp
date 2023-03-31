from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class LoginForm(forms.Form):
	username = forms.CharField(label = "username", max_length = 20)
	password = forms.CharField(label = "password", max_length = 20)

class AddTaskForm(forms.Form):
	task_name = forms.CharField(label = 'task_name', max_length =50)
	description = forms.CharField(label = 'description', max_length = 200)

class UpdateTaskForm(forms.Form):
	task_name = forms.CharField(label = "task_name", max_length = 50 )
	description = forms.CharField(label = "description", max_length = 200)
	status = forms.CharField(label = "status", max_length = 50)

class EventItemForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=200, required=True)
    start_time = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}), required=True)
    end_time = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}), required=True)