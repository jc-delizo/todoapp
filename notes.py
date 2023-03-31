# [Section] Models
# Each model is represented by a class that inherits the django.db.models.Model. Each model has a number of class variables, ecah of which represents a database field in the model.
# Each field is represented by an intance of a field class eg charfield for character fields and DateTimeFIeld for date times. This telss django what type of data each field holds.
# Some field classes have required arguments. CharField requires that you give it a max_length.
# A field can also have various optional arguments; in this case, we've set the default value of status to pending

# [Section] Migration
python manage.py makemigrations todolist
# by running makemigrations, you're telling django that you've made some changes to your models

# migrate
python manage.py sqlmigrate todolist 0001
python manage.py migrate

# to run the python Shell
python manage.py shell

todoitem = ToDoItem(task_name = "Eat", description = "Dinner", date_created = timezone.now())

# save
todoitem.save()

# for the mysql connection
pip install mysql_connector
pip install mysql

# or
pip install mysql_connector mysql

# creating superuser
# macOs/linux
python3 manage.py createsuperuser

# windows
winpty python manage.py createsuperuser

