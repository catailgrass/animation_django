from django.shortcuts import render
from utils.sql_manage import *
from django.http import HttpResponse, Http404
import json


# Create your views here.

def show_animation(request):
    if request.method == 'GET':
        arry = get_all_animation()
        ret = json.dumps(arry)
        return render(request,'show_anime.html')
