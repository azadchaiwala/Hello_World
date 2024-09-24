from django.http import HttpResponse

# Create your views here.
def homeView(request):
    message='Hello Husnain'


    return HttpResponse(message)

def aboutView(request):
    message=('this is about section of our project')

    return HttpResponse(message)

def footerview(request):
    message=('this is footer section')

    return HttpResponse(message)