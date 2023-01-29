from django.shortcuts import render

def Preview(request):
    return render(request, 'Preview.html')
