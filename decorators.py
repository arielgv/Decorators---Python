# Decorators: A decorator is a design pattern in Python that allows a user to 
# add new functionality to an existing object without modifying its structure. 
# Decorators are usually called before the definition of a function you want to decorate.


def decorator(function1):
    def decorator2():
        function1()
        print("this line contains a text, for example.")
    
    return decorator2

@decorator
def principal():
    print("This line es the decorator , in this case. ")
principal()


# Code writted in Visual Studio Code.  