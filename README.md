# backend
<p>
Steps to set up venv:-
    1.Install uv if not by (pipx install uv) [pipx is more usefull to download tools]
    2.Create a new venv by (uv venv)
    3.Activate the venv by (.venv/Scripts/activate)

step to start server:-
    1.Check if you have django installed or not by ( pip show django or where django)
        [it should show the path ]
    2.If django is not installed in you venv then install it by (pip install django)
    3.Now to start a new project run (django-admin startproject project_name .) command in terminal
    4.The previous command will create a floder of project_name and a manage.py file
    5.Now to run server run (python manage.py runserver) command in terminal.
    6.You can ignore the simple warning and just copy the server path/code provided and past it into the  broswer

[To use a html file on your web you have to first add the file dir in templates dirs in setting.py file in project_name folder]

[Use from django.shortcut import render command to use template ]
[create a function in views.py file  example
    def home(request):
        request render(request, 'file_name.html')]

Steps to include css:-
    1.Create a static file in which you will make js and css file
    2.Create a css file and add the desire css
    3.Use lick tag in your html file usual but on the place of file name use loader for example
        {%static 'file_name.css'%} 
    4.Add loader on the top of the html file even above doctype by
        {%load static%}

    5.Now add the static folder into the static dirs by following steps:-
            5.1.First go to setting.py in project_file
            5.2.Look for static setting probably near bottom
            5.3.Below the STATIC_URL = 'static/' line add a new line as follow
                STATICFILES_DIRS = [
                    BASE_DIR / "static",  # Directory for static files
                    ] 
            5.4.Save everthing and it's all set to go  
              
        <p\>      