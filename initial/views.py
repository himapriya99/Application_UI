from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
data = {}
def input (request):  
    data = {}
    rel_target = [{"release": "FW22-FW15-0802"},{"release": "FW22-FW17-0804"}]
    data['r'] = rel_target
    print(data)
    return render( request, "initial/input.html",data)

def submit(request):
    #data = {}
    table=[]# get data into table variable from models ex: table = <Model_name>.objects.all()
    sap_rwi = '10796272'
    myq_rwi = '10722773'
    sap_crq = 'CHG0363605'
    myq_crq = 'CHG0363606'
    if request.method == "POST":
        release = str(request.POST.get('Release'))
        lock = request.POST.get('radiobutton')
        data['release'] = release
        data['lock'] = lock
        data['t'] = table
        data['sap_rwi'] = sap_rwi
        data['myq_rwi'] = myq_rwi
        data['sap_crq'] = sap_crq
        data['myq_crq'] = myq_crq
        print(release)
        print(lock)
        print(data)
        #getting all stories from tfs using release into DB
    if data['lock'] == "scopelock":
       return render(request, "initial/scopel.html", data)
    elif data['lock'] == 'codelock':
       return render( request, "initial/codel.html",data)
    else :
       return render( request, "initial/input.html")

def scope_alert(request):
     alert = '1'
     data['alert'] = alert
     alert = '0'
    # return render(request,"initial/scopel.html",data)
     return render(request,"initial/pop.html",data)
def code_alert(request):
    #validations and email code for code lock
   # return HttpResponse('codelock')#popup page
   return redirect("code_alert")

def download(request):
    
    return redirect(request. META['HTTP_REFERER']) 


