# anonymous function is defined using lambda keyword
# it can contain only one line of code
get_color_lambda = lambda self: f"My color: {self.color}"

def get_color_func(self):
    return f"My color: {self.color}"

# lambda is pretty much the same as usual function and can be used in any place function is used
type(get_color_lambda) # function
type(get_color_func) # function

class Vehicle:
    def __init__(self, color, 
        lambda_getter = get_color_lambda, 
        func_getter = get_color_func
    ):
        self.color = color
        self.get_color_lambda = lambda_getter
        self.get_color_func = func_getter

    def get_color_method(self):
        return f"My color: {self.color}"


red_vehicle = Vehicle('red')

# method has it's own type 'method'
type(red_vehicle.get_color_method) # method

# main difference between function and method that method has implicit first parameter 
# - self - the object on which method was called
red_vehicle.get_color_method() # My color: red
red_vehicle.get_color_func(red_vehicle) # My color: red
red_vehicle.get_color_lambda(red_vehicle) # My color: red

