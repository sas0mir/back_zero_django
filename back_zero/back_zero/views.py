from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Test response for homepage")
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')