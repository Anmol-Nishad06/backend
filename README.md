# backend
<p>
<h3> Steps to set up venv:- </h3>
    <ol>
    <ls>Install uv if not by (pipx install uv) [pipx is more usefull to download tools] </ls>
    <ls>Create a new venv by (uv venv)</ls>
    <ls>Activate the venv by (.venv/Scripts/activate)</ls>
    </ol>

<h3>step to start server:-</h3>
    <ol>
    <ls>Check if you have django installed or not by ( pip show django or where django)
        [it should show the path ]</ls>
    <ls>If django is not installed in you venv then install it by (pip install django)</ls>
    <ls>Now to start a new project run (django-admin startproject project_name .) command in terminal</ls>
    <ls>The previous command will create a floder of project_name and a manage.py file</ls>
    <ls>Now to run server run (python manage.py runserver) command in terminal.</ls>
    <ls>You can ignore the simple warning and just copy the server path/code provided and past it into the  broswer</ls>
    </ol>

[To use a html file on your web you have to first add the file dir in templates dirs in setting.py file in project_name folder]

[Use from django.shortcut import render command to use template ]
[create a function in views.py file  example
    def home(request):
        request render(request, 'file_name.html')]

<h3>Steps to include css:-</h3>
    <ol>
    <ls>Create a static file in which you will make js and css file</ls>
    <ls>Create a css file and add the desire css</ls>
    <ls>Use lick tag in your html file usual but on the place of file name use loader for example
        {%static 'file_name.css'%} </ls>
    <ls>Add loader on the top of the html file even above doctype by
        {%load static%}</ls>

    <ls> Now add the static folder into the static dirs by following steps:- </ls>
            <ul>
            <ls>First go to setting.py in project_file. </ls>
            <ls>Look for static setting probably near bottom</ls>
            <ls>.Below the STATIC_URL = 'static/' line add a new line as follow
                STATICFILES_DIRS = [
                    BASE_DIR / "static",  # Directory for static files
                    ] 
            <ls>Save everthing and it's all set to go  </ul>
    </ol>      

<h3>Steps to install Tailwind:- </h3>
    <ol>
        <ls>Run "python -m pip install django-tailwind" command interminal to initiate tailwind download.    </ls> 
        <ls> Now run "python -m pip install 'django-tailwind[reload]'" in terminal to download auto reload package</ls>
        <ls>Now go to the setting.py file in core folder and add 'tailwind' in the installed app option </ls> 
        <ls>Now to download css theme file into folder run "python manage.py tailwind init" </ls>
        <ls> Now go to the setting.py file in core folder and add 'theme' or the name of the file you gave in the installed app option </ls> 
        <ls> Register the generated 'theme' app by adding the following line to settings.py:
            [TAILWIND_APP_NAME = 'theme']</ls> 
        <ls>Install Tailwind CSS dependencies by running "python manage.py tailwind install" </ls>
        <ls>Now go to the setting.py file in core folder and add '"django_browser_reload.middleware.BrowserReloadMiddleware"'in the MIDDLEWARE option (it will help in auto reload).  </ls></ol>

<h3>How to use tailwind :-</h3>
    <ol>
    <ls>To use tailwind in your layout add a load tag on top as {%load static tailwind_tag %} </ls>
    <ls>Now add link to tailwind css in head section as {% tailwind_css %}</ls></ol>

<h3>How to run tailwind:-</h3>
    <p>to run tailwind use to different server one for python and another for tailwind by creating a new terminal run "python manage.py tailwind dev" so the tailwind server will work  simultaneously with python one</p>



        <p\>      