from django.shortcuts import render

# Create your views here.
def hello(request):
    context = {'hello': 'Hello, Heroku!'}
    return render(request, 'hello.html', context)