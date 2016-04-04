README

INTRODUCTION
------------

This project will help you find your current location or locate a given street address on a Google map. Django Framework and Python3, used for backend. Bootstrap, HTML, CSS, JavaScript, jQuery are used for frontend. Google Map API has been used to locate address on a Google map.


REQUIREMENTS
------------

To run this project, you would need to have python3 and Django. Refer https://www.python.org/downloads/ and https://www.djangoproject.com/download/ for download details. To ensure you have installed them correctly, you can check by executing the following command,

$python
>>import django
>>

Inappropriate installation would throw an error for ‘import django’
For more information on installation, you may check https://docs.djangoproject.com/en/1.9/topics/install/


CODE FILES
----------

Project Name – mySite
App Name – findlocation

HTML files located in templates directory
header.html – Consists of common html template for home.html and streetLocation.html
home.html - Consists of html page to get current location
streetLocation - Consists of html page to locate a street address on map

Bootstrap & image files located in static directory


EXECUTING THE PROJECT
---------------------


Project Name - mySite

Execute the following commands:
cd mySite/
python manage.py runserver

If executed correctly, you would see

Performing system checks...
System check identified no issues (0 silenced).
April 04, 2016 - 00:14:39
Django version 1.9.4, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

You would need to open your browser and type in http://127.0.0.1:8000/


CONTACT
-------
For any issues related to this project, please contact pranjalj@usc.edu

