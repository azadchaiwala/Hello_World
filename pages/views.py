from django.http import HttpResponse

# Create your views here.
def homeView(request):
    message='Hello Husnain'


    return HttpResponse(message)

def aboutView(request):
    message=('this is about section of our project')

    return HttpResponse(message)

def contactView(request):
    message=('this is contact section')

    return HttpResponse(message)

def cartView(request):
    message=('this is a cart section')

    return HttpResponse(message)
