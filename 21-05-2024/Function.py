# function
# arguments
# parameters
# return type
# non return type
# function have parameters/arguments
# function don't have parameters/arguments


# Define Function
def hello():  # No Parameter/No Arguments,No Return type
    print("Hello")


hello()


def say_hello_arg(name):  # With single Argument,No Return type
    print("Hello", name)


# calling function
say_hello_arg("sharan")


def say_hello_args(name, age):  # multiple_args,No return type
    print("Hello", name, age)


say_hello_args("sharan", 25)


# defaultvalue
def say_hello_arg_default(name="Dhoni"):  # default_args,No return type
    print("Hello", name)


say_hello_arg_default()


# Return type

def addition(num1, num2):
    print("Addition")
    return num1 + num2


result = addition(3, 4)
result2 = addition("sharan", "Ravi")
print(result2)


# *args
def make_pizza(*toppings):
    for topping in toppings:
        print(topping)


sharan = make_pizza("mushroom", "onion", "tomatto")

#base
def make_pizza_base(*topings,base):
    print(topings,base)
    for toping in topings:
        print(toping)


sharan = make_pizza_base("mushroom", "onion", "tomatto",base="thin")







