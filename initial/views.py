from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
data = {}
data['message'] = None
def input (request):  
    return render( request, "initial/input.html")

def submit(request):
    #data = {}
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
    if data['lock'] == "scopelock":
       return render(request, "initial/scopel.html", data)
    elif data['lock'] == 'codelock':
       return render( request, "initial/codel.html",data)
    else :
       return render( request, "initial/input.html")

def scope_alert(request):
    #validations and email code for scope lock
   # return HttpResponse('scopelock')#popup page
   
     #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
     #return redirect(request,"initial/scopel.html",context)
     return render(request,"initial/pop.html",data)

def code_alert(request):
    #validations and email code for code lock
    return HttpResponse('codelock')#popup page


