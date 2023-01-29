from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def reverse(request):
    old_text = request.GET['usertext']
    kol_slov = len(old_text.split(' '))
    new_text = old_text[::-1]
    print(request.GET)
    return render(request, 'reverse.html', {'old_text' : old_text, 'new_text' : new_text, 'kol_slov' : kol_slov})

