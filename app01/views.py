from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def user_list(request):
    return render(request, 'user_list.html')

def user_add(request):
    return HttpResponse('Add_user')

def tpl(request):
    name = 'sherlock'
    
    return render(request, 'tpl.html', {'n1': name})