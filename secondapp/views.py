from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def getIndexPage3(request):
    msg = """
        <b>
        firstapp 내에 views.py의 getindex3가 호출되었습니다.
        </b>
    """
    return HttpResponse(msg)
