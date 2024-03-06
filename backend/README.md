1. Install python
2. Create virtual environment (venv) `python -m venv venv`
3. Activate venv `.\venv\Scripts\activate`
4. install django `pip -m install Django`
5. Start project inside backend folder `django-admin startproject app .`
6. Start and check server `python .\manage.py runserver`
7. Migrate initial models (users, groups) `python .\manage.py migrate`
8. Create pages application `python .\manage.py startapp pages`
9. Add 'pages' app into settings.py INSTALLED_APPS
10. 
11. 
12. 
13. 

### Common commands
`python .\manage.py runserver` - run server
`python .\manage.py makemigraions` - Create migrations 
`python .\manage.py migrate` - Apply created migrations
`python .\manage.py startapp pages` - Create new application