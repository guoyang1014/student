from django.http import HttpResponse
from django.shortcuts import render_to_response

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'a' in request.GET:
        message = '你搜索的内容为:'+ request.GET['a']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)