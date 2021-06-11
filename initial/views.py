from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def input (request):  
    return render( request, "initial/input.html")
def submit(request):
    data = {}
    if request.method == "POST":
        title = request.POST.get('Release')
        print(title)
    return render(request, "initial/stories.html", data)


