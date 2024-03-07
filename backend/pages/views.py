from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from pages.models import Page

def get_pages(request):
    pages = Page.objects.all() # взяли все объекты
    pages_list = [] # создали пустой список
    for page in pages:
        pages_list.append({
            "id": page.id,
            "title": page.title,
            "description": page.description,
            "h1": page.h1,
            "created_at": page.created_at,
            "updated_at": page.updated_at,
            "path": page.path,
        })
    return JsonResponse(
        pages_list, safe=False
    )


def get_page(request, path):
    print(path)
    page = get_object_or_404(Page, path=path)
    serialized_page = {
        "id": page.id,
        "title": page.title,
        "description": page.description,
        "h1": page.h1,
        "created_at": page.created_at,
        "updated_at": page.updated_at,
    }
    return JsonResponse(
        serialized_page, safe=False
    )
