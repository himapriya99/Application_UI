from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def input (request):  
    return render( request, "initial/input.html")

def submit(request):
    data = {}
    table=[]# get data into table variable from models ex: table = <Model_name>.objects.all()
    if request.method == "POST":
        release = str(request.POST.get('Release'))
        lock = request.POST.get('radiobutton')
        data['release'] = release
        data['lock'] = lock
        data['t'] = table
        print(release)
        print(lock)
        #getting all stories from tfs using release into DB
    if lock == "scopelock":
       return render(request, "initial/scopel.html", data)
    elif lock == 'codelock':
       return render( request, "initial/codel.html",data)
    else :
       return render( request, "initial/input.html")

def scope_alert(request):
    #validations and email code for scope lock
    return HttpResponse('scopelock')#popup page

def code_alert(request):
    #validations and email code for code lock
    return HttpResponse('codelock')#popup page


