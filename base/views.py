from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Todo
# Create your views here.

def home(request):

    todo_list = Todo.objects.all()
    if request.method == 'POST':
        print("###########################################################")
        print(request.POST)

        if 'input_but' in request.POST:
            print('ONE')
            inputText = request.POST.get('inputText')
            Todo.objects.create(
                task = inputText
            )
            return redirect('home')
        elif 'del_but' in request.POST:
            print('TWO')
            todo = request.POST.get('del_but')
            print(todo)
            todo = Todo.objects.filter(pk=todo)
            todo.delete()
            return redirect('home')
        # inputText = request.POST.get('inputText')
        # Todo.objects.create(
        #     task = inputText
        # )
        # return redirect('home')

    context = {'todo_list':todo_list}
    return render(request, 'index.html', context)

def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
