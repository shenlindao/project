1. Install python
2. Create virtual environment (venv) `python -m venv venv`
3. Activate venv `.\venv\Scripts\activate`
4. install django `pip -m install Django`
5. Start project inside backend folder `django-admin startproject app .`
6. Start and check server `python .\manage.py runserver`
7. Migrate initial models (users, groups) `python .\manage.py migrate`
8. *Create pages application `python .\manage.py startapp pages`
9. Add 'pages' app into settings.py INSTALLED_APPS
10. Add index into pages/views.py
10. Add urls.py into pages and register index view
11. Register pages/urls.py in app/urls.py
12. Create Page model in pages/models.py
13. Create first Page model implementation
14. Make migration `python .\manage.py makemigrations`
15. Apply migration `python .\manage.py migrate`
16. Register Page model in pages/admin.py 
17. Delete test view.py
18. Create get_pages view
18. Create get_page view for single page by uid

### Common commands
`python .\manage.py runserver` - run server
`python .\manage.py makemigrations` - Create migrations 
`python .\manage.py migrate` - Apply created migrations
`python .\manage.py startapp pages` - Create new application