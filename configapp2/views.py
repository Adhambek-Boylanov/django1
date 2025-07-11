from django.shortcuts import render

from django.http import JsonResponse
def json_qaytar(request):
    return JsonResponse({"Anvar":21,"Bobur":23,"Qobil":12,"Elbek":18})
