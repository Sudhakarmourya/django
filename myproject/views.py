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
def about(request):
    return render(request,'about.html')
# def course(request):
#     return HttpResponse('Welcome to our courses page')
# def courseDetails(request,courseid):
#     return HttpResponse(courseid)
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def faq(request):
    return render(request, 'faqs.html')
def services(request):
    return render(request, 'service.html')
def privacy(request):
    return render(request, 'privacy-policy.html')
def site(request):
    return render(request, 'site-map.html')
def term(request):
    return render(request, 'terms-condition.html')
def error(request):
    return render(request, 'error.html')