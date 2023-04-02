from django.urls import path
# import the views.py from the same folder
from . import views


app_name = 'todolist'

urlpatterns = [
	path('index', views.index, name = 'index'),
	path('<int:todoitem_id>/', views.todoitem, name = "viewtodoitem"),
	path('register', views.register, name = "register"),
	path('change_password', views.change_password, name = "change_password"),
	path('login', views.login_user, name = "login"),
	path('logout', views.logout_user, name = "logout"),
	path('add_task', views.add_task, name = "add_task"),
	path('add_events', views.add_events, name = "add_events"),
	path('<int:todoitem_id>/update_task', views.update_task, name = "update_task"),
	path('<int:todoitem_id>/delete', views.delete_task, name = "delete_task")
]