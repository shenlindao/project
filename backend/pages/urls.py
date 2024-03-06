from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_pages, name="get_pages"),
    path("<str:page_id>", views.get_page, name="get_page"),
]