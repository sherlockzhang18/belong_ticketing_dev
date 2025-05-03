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


from app01.models import UserInfo, Department
def info_list(request):
    # get all the user info from sql
    data_list = UserInfo.objects.all()
    for obj in data_list:
        # get the department info
        print(obj.name, obj.password, obj.age)
    
    # UserInfo.objects.all().update(id = 1, name='sherlock')
    
    return render (request, 'info_list.html', {'data_list': data_list})

def info_add(request):
    if request.method == 'GET':
        return render(request, 'info_add.html')
    user = request.POST.get('name')
    pwd = request.POST.get('password')
    age = request.POST.get('age')
    
    # add to the database
    UserInfo.objects.create(name=user, password=pwd, age=age)
    
    return redirect('/info/list/')