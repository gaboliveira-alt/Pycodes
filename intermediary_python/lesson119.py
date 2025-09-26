from lesson119_package.module import add_task, remove_task, redo_task, print_tasks, is_string, save_taskfile, read_tasks


while True:
    print('Comandos: listar, refazer, desfazer.')
    user_input = input('Digite uma tarefa ou um comando: ').lower()
    is_string(user_input)
    print()
    
    
    commands = {
        'listar': lambda: print_tasks(),
        'desfazer': lambda: remove_task(),
        'refazer': lambda: redo_task(),
        'adicionar': lambda: add_task(user_input),
    }
    
    command = commands.get(user_input) if commands.get(user_input) is not None else \
        commands['adicionar']
    command() # pyright: ignore[reportOptionalCall]
    save_taskfile()