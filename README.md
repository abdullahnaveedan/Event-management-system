# Getting started with Django on Google Cloud Platform on App Engine Standard

[![Open in Cloud Shell][shell_img]][shell_link]

[shell_img]: http://gstatic.com/cloudssh/images/open-btn.png
[shell_link]: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&page=editor&open_in_editor=appengine/standard_python38/django/README.md

This repository is an example of how to run a [Django](https://www.djangoproject.com/) 
app on Google App Engine Standard Environment. It uses the 
[Writing your first Django app](https://docs.djangoproject.com/en/3.2/intro/tutorial01/) as the 
example app to deploy.


# Tutorial
See our [Running Django in the App Engine Standard Environment](https://cloud.google.com/python/django/appengine) tutorial for instructions for setting up and deploying this sample application.

1:-
env\Scripts\activate

2:-
pip install -r requirements.txt

3:-
pip install -r requirements-test.txt

4:-
cloud-sql-proxy.exe alfred-event-manager-00001:us-central1:event-management-00001

5:-
set GOOGLE_CLOUD_PROJECT=alfred-event-manager-00001

6:-
gcloud auth list //choose email address 

7:-
set USE_CLOUD_SQL_AUTH_PROXY=true

8:-
python manage.py runserver

9:-
127.0.0.1:8000 or localhost:8000
