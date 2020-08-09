# User Activity App
This django application outputs all the users with their activity durations.

## Create dummy activities
Use the below management command to generate dummy user activities for all the users available in the database.

Use this to create 5 dummy user activities
```
python manage.py adddummyactivity 
```

Or use this to create dummy activities as required
```
python manage.py adddummyactivity num_of_activities
```
change ```num_of_activities``` to any number below 20 to create activities.

Example:
 ```
python manage.py adddummyactivity 10
```
This will generate 10 activities per user.