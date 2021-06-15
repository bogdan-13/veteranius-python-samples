# global variable is visible in inner scopes
name_global = 'Alina'

def greet():
    print("Hello ", name_global)

def greet():
    # local variable is visible only inside greet function
    name = 'Yuliya'
    print('Hello ', name)


name_global = 'Alina'

def greet():
    name_inner = 'Yulia'   

    def inner_greet():
        # if we want to change global variable global keyword is used
        global name_global
        # if we want to change variable from the outer scope nonlocal keyword is used
        nonlocal name_inner
        name_global = 'Stephan'
        print(f'Inner inner: {name_global}')

    inner_greet()
    print(f'inner: {name_inner}')

greet()
print(f'Outer: {name_global}')

