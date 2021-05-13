def outer_function(a, b):

    def inner_function():
        addition = a + b
        return addition

    return 5 + inner_function()


print(outer_function(5, 3))