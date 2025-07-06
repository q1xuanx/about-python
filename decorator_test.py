# Decorator
def main_welcome(func): 

    def sub_welcome_method ():
        print('Hello World')
        func()
        print('Good Bye')
    
    return sub_welcome_method

@main_welcome
def course_hello():
    print('Say hello ??')

course_hello()

# Decorator with Arguments 

def repeat(n):
    def decorator(func): 
        def wrapper(*args, **kwargs):
            args_list = list(args)
            kwargs['age'] = kwargs['age'] + 10
            print(args_list[0])
            func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello(name, age):
    print(f'Hello {name} - {age}')

say_hello('Nhan', age=20)