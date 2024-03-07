from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import Order

def order_list(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        new_order = Order(
            name=data['order_name'],
            phone=data['order_phone'],
            email=data['order_email'],
            created_at=data['created_at']
        )
        new_order.save()

        response_data = {
            'message': 'Данные успешно сохранены',
            'data': data
        }
        
        return JsonResponse(response_data)

    return HttpResponse('Метод GET не поддерживается')