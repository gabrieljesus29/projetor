from django.shortcuts import render
from django.http import JsonResponse

def estudantes(request):
    if request.method == 'GET':
        estudante = {
            'id': '1234',
            'nome': 'Maria'
        }
    return JsonResponse(estudante)
