

def what_are_the_vars(*args, **kwargs):
    """
    ...
    """
    
    if any(f"var_{i}" in kwargs for i in range(len(args))):
        return None
    obj = ObjectC()
    obj.__dict__.update(kwargs)
    obj.__dict__.update({f"var_{i}": args[i] for i in range(len(args))})
    return obj
    


class ObjectC(object):
    def __init__(self):
        # ... Your code here ...
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


# if __name__ == "__main__":
#     obj = what_are_the_vars(7)
#     doom_printer(obj)
#     obj = what_are_the_vars(None, [])
#     doom_printer(obj)
#     obj = what_are_the_vars("ft_lol", "Hi")
#     doom_printer(obj)
#     obj = what_are_the_vars()
#     doom_printer(obj)
#     obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
#     doom_printer(obj)
#     obj = what_are_the_vars(42, a=10, var_0="world")
#     doom_printer(obj)
#     obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
#     doom_printer(obj)
# if __name__ == "__main__":
# 	obj = what_are_the_vars(7)
# 	doom_printer(obj)
# 	obj = what_are_the_vars("ft_lol", "Hi")
# 	doom_printer(obj)
# 	obj = what_are_the_vars()
# 	doom_printer(obj)
# 	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
# 	doom_printer(obj)
# 	obj = what_are_the_vars(42, a=10, var_0="world")
# 	doom_printer(obj)
# 	obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
# 	doom_printer(obj)