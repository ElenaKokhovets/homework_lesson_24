from django.shortcuts import render
from .models import Project

def project_index(request): #индексное представление всех постов
    vse_posti = Project.objects.all() #в переменную vse_posti собрали все посты в таблице Project
    context = {
        'vse_posti':vse_posti
    } #закидываем в переменную словарь
    return render(request, 'project_index.html', context)

def project_detail(request,pk): #id первичный ключ конкретного поста
    odin_post = Project.objects.get(pk=pk) #в переменную odin_post собрали пост с первичным ключом равным id из таблицы Project
    context = {
        'odin_post':odin_post
    } #закидываем в переменную словарь
    return render(request, 'project_detail.html', context)