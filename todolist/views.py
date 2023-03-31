from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

# The from keyword allows importing of necessary classes/modules, methods and others files needed in our application from the django.http package while the import keyword defines what we are importing from the package
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Local imports
from .models import ToDoItem, EventItem

# import the built in User Model
from django.contrib.auth.models import User

# to use the template created:
# from django.template import loader

# import the authenticate function
from django.contrib.auth import authenticate, login, logout

from django.forms.models import model_to_dict

from .forms import LoginForm, AddTaskForm, UpdateTaskForm, RegistrationForm, EventItemForm

from django.utils import timezone

def index(request):
	todoitem_list = ToDoItem.objects.filter(user_id = request.user.id)
	# template = loader.get_template("index.html")
	context = {
		'todoitem_list': todoitem_list,
		"user": request.user
	}
	# output = ", ".join([todoitem.task_name for todoitem in todoitem_list])
	# render(request, route_template, context)
	return render(request, "index.html", context)

def todoitem(request, todoitem_id):
	# response = f"You are viewing the details of {todoitem_id}"
	# return HttpResponse(response)

	todoitem = get_object_or_404(ToDoItem, pk = todoitem_id)

	return render(request, "todoitem.html", model_to_dict(todoitem))

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                # check if the user already exists in the database
                if User.objects.filter(username=username).exists():
                    form.add_error('username', 'This username is already taken.')
                else:
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                    user.is_staff = False
                    user.is_active = True
                    user.save()

                    context = {
                        'is_user_registered': True,
                        'first_name': first_name,
                        'last_name': last_name
                    }
                    return render(request, "login.html", context)
            else:
                form.add_error('password2', 'Passwords do not match.')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def change_password(request):

	is_user_authenticated = False

	user = authenticate(username = "johndoe", password = "johndoe123456")

	if user is not None:
		authenticated_user = User.objects.get(username = 'johndoe')
		authenticated_user.set_password("johndoe1234567")
		authenticated_user.save()

		is_user_authenticated = True

	context = {
		"is_user_authenticated" : is_user_authenticated
	}

	return render(request, "change_password.html", context)

def login_user(request):
	context = {}

	# if this is a post request we need to process the form data
	if request.method == "POST":

		form = LoginForm(request.POST)

		if form.is_valid() == False:
			form = LoginForm()
			
		else:
			print(form)
			# cleaned_data retrieves the information from the form
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username = username, password = password)

			if user is not None:
				context = {
					'username' : username,
					'password' : password
				}
				login(request, user)
				return redirect("todolist:index")
			else:
				context = {
					'error' : True
				}
			
	
	return render(request, "login.html", context)








	# username = 'johndoe'
	# password = 'johndoe1234567'

	# user = authenticate(username = username, password = password)

def logout_user(request):
	logout(request)
	return redirect("todolist:index")

def add_task(request):
	context = {}

	if request.method == 'POST':
		form = AddTaskForm(request.POST)

		if form.is_valid() == False:
			form = AddTaskForm()

		else:
			task_name = form.cleaned_data['task_name']
			description = form.cleaned_data['description']

			duplicates = ToDoItem.objects.filter(task_name = task_name, user_id = request.user.id)

			if not duplicates:
				# create an ovbject based on the ToDoItem model and saves to the record in the database

				ToDoItem.objects.create(task_name = task_name, description = description, date_created = timezone.now(), user_id = request.user.id)

				return redirect("todolist:index")
			else:
				context = {
					'error' : True
				}

	return render(request, "add_task.html", context)

def update_task(request, todoitem_id):
	todoitem = ToDoItem.objects.filter(pk = todoitem_id)
	print(todoitem)
	context = {
		"user": request.user,
		"todoitem_id": todoitem_id,
		"task_name": todoitem[0].task_name,
		"description": todoitem[0].description,
		"status": todoitem[0].status
	}
	if request.method == "POST":
		form = UpdateTaskForm (request.POST)
		
		if form.is_valid() == False:
			form = UpdateTaskForm()
		else:
			task_name = form.cleaned_data['task_name']
			description = form.cleaned_data['description']
			status = form.cleaned_data['status']

			if todoitem:
				todoitem[0].task_name = task_name
				todoitem[0].description = description
				todoitem[0].status = status

				todoitem[0].save()

				return redirect("todolist:viewtodoitem", todoitem_id = todoitem[0].id)
			else:
				context = {
					"error": True
				}
	return render(request, "update_task.html", context)

def delete_task(request, todoitem_id):

	ToDoItem.objects.filter(pk = todoitem_id).delete()

	return redirect('todolist:index')

def add_event(request):
    if request.method == 'POST':
        form = EventItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            user_id = request.user.id

            # Check if there are any overlapping events
            overlapping_events = EventItem.objects.filter(user_id=user_id, start_time__lt=end_time, end_time__gt=start_time)
            if overlapping_events.exists():
                return redirect('add_event')

            # Create new event if no overlaps
            event = EventItem(name=name, description=description, start_time=start_time, end_time=end_time, user_id=user_id)
            event.save()
            return redirect('add_event')

    else:
        form = EventItemForm()

    context = {
        'form': form,
    }

    return render(request, 'add_event.html', context)