import json


PATH_FILE = 'C:\\Users\\kylor\\OneDrive\\Documentos\\GitHub\\Pycodes\\example_pathfile\\'
PATH_FILE += 'lesson119.json'
todo_list = []
redo_tasks = []


def is_string(user_input):
    if not isinstance(user_input, str):
        raise TypeError(f'{user_input} não é um texto, as tarefas precisam ser escritas como texto.')


def is_list(todo_list):
    if not isinstance(todo_list, list):
        raise TypeError(f'{todo_list} deve ser uma lista para criar as tarefas.')    


def add_task(user_input):
    is_list(todo_list)
    has_nothing = user_input.strip()
    if not has_nothing:
        raise Exception('Você não digitou nenhuma tarefa')
    todo_list.append(user_input)


def remove_task():
    is_list(todo_list)
    if len(todo_list) < 1:
        print('Não há nada para remover')
        
    last_value = todo_list.pop()
    redo_tasks.append(last_value)
    return
    

def redo_task():
    is_list(todo_list)
    if len(todo_list) < 1:
        print('Não há nada para refazer')
        
    last_task = redo_tasks.pop()
    add_task(last_task)


def print_tasks():
    is_list(todo_list)
    if len(todo_list) >= 1:
        print()
        print('TAREFAS:')
        print(*todo_list, sep='\n')
        print()
    else:
        print('NÃO HÁ NADA PARA LISTAR')
        print()


def read_tasks():
    data_tasks = []
    try:
        with open(PATH_FILE, 'r', encoding='utf-8') as task_file:
            data_tasks = json.load(task_file)
    except FileNotFoundError:
        print('Arquivo não existe')
        save_taskfile()
    return data_tasks


def save_taskfile():
    data_tasks = todo_list
    
    with open(PATH_FILE, 'w', encoding='utf-8') as task_file:
        data_tasks = json.dump(data_tasks, task_file, indent=2, ensure_ascii=False)
    return data_tasks