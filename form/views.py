# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from form.models import Post
from form.forms import PostForms


# либо post_all или post_list
def post_list(request):
    '''
    вывод всех записей
    '''
    to = Post.objects.all()
    return render_to_response('post_list.html', {'to': to})

def post_new (request):
    # указываем метод которым создавать форму
    if request.method == 'POST':
        # укажем с какой формой работать
        form = PostForms (request.POST)
        if form.is_valid(): # проверить данные
            print form.cleaned_data # все что-то правильно заполнено
            post = form.save(commit=False)
            # commit=False указывается когда нужны необходимые дополнительные действия
            # например форма будет ждать пока не нажмете кнопку отправить
            post.author = request.user # джанго берет из сесии пользователя,
            #вы зашли в кабинет и отображается ваш логин т.е. происходит взаимодействие с сайтом
            post.save() # и сохраняем этого пользователя
            return redirect ('formsa:post_detali', pk = post.pk) # страница формы, и ид именно этой записи
    else:
        form = PostForms

    return render(request, 'post_edit.html', {'form': form}) # ну и вывести

def post_detali (request, pk):
    post = get_object_or_404(Post, pk=pk)# (Post, pk=pk) pk это как id,
    # вывести либо ошибку либо функцию
    return render(request, 'post_detali.html', {'post': post}) # вернуть, показать, и вывести в html файл.

def post_edit (request, pk): # это функция для редактирования
    post = get_object_or_404(Post, pk=pk) # выводит запрос
    if request.method == 'POST': # добавить методом POST
        form = PostForms(request.POST, instance=post)# instance=post это объект, можно и вася
        if form.is_valid(): # проверка формы на валидность
            post = form.save (commit=False)# сохранить и ждать кнопку
            post.author = request.user #опеределить автора
            post.save () # сохранить изменения
            return redirect ('formsa:post_detali', pk = post.pk) # вернуть и перевести на страницу редирект(написаного поста)
    else:
        form = PostForms(instance=post) #иначи вернуть форму обратно
        # instance=post т.е. вернуть нам не запись а обхект который мы редактируем
    return render(request, 'post_edit.html', {'form': form}) #вернуть показать запрасить вывести html
