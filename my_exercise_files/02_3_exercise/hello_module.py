import names_module

def say_hello(names_list):
    for name in names_list:
        print(f'Hello, {name}')

say_hello(names_module.names)