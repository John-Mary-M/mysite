from django.shortcuts import render

def homepage(request):
    '''homepage function'''
    return render(request, 'home.html')

def about(request):
    '''processes the about page'''
    return render (request, 'about.html')
