from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    data = {
        'title':'Home Page',
        'bdata':'welcome to Wscubetech',
        'clist':['PHP','JAVA','PYTHON','ANDROID'],
        'number':[40],
        'student_list':[
            {'name':'sudhakar','phone':'7800006656'},
             {'name':'Neha','phone':'7839336240'}
        ]
    }
    return render(request,'index.html',data)
def aboutUs(request):
    return HttpResponse('welcome to Techsima  Solution Private limited')
def course(request):
    return HttpResponse('Welcome to our courses page')
def courseDetails(request,courseid):
    return HttpResponse(courseid)