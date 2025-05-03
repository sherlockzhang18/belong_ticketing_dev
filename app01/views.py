from django.shortcuts import render, HttpResponse, redirect

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

def login(request):    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == 'admin' and password == '123':
            return redirect("http://www.google.com")
        
        return render(request, 'login.html', {'error_msg': 'Invalid username or password!'})
    
    return render(request, 'login.html')