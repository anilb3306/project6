from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':200,'b':400,'c':600}
    return render(request,'a2_first.html',d)

def a2_second(request):
    d={'name':'anil'}
    return render(request,'a2_second.html',d)