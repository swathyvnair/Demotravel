from django.http import HttpResponse
from django.shortcuts import render
from . models import Team
# Create your views here.
def abcd(request):
    xyz=Team.objects.all()
    return  render(request,"index.html",{'result':xyz})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     s=x-y
#     m=x*y
#     d=x/y
#     return render(request,"result.html",{'result':res,'result1':s,'result2':m,'result3':d})
#

