from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_pages, name="get_pages"),
    path("<path:path>", views.get_page, name="get_page"),
]