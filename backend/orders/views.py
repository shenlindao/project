from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Order

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            new_order = Order(
                name=data['order_name'],
                phone=data['order_phone'],
                email=data['order_email'],
            )
            new_order.save()

            response_data = {
                'message': 'Данные успешно сохранены',
                'id': new_order.id
            }

            return JsonResponse(response_data)

        except KeyError:
            return JsonResponse({'error': 'Invalid request body'}, status=422)


    return HttpResponse('Используйте только POST запрос')