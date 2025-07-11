from django.shortcuts import render

from django.http import JsonResponse
def salom_django(request):
    return JsonResponse({"Adhambek":19,"Abbos":20,"Rustam":25,"Umar":20})
