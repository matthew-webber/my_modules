def one():
    return 'Complete'

def two():
    pass

def three():
    pass

def four():
    pass

def five():
    pass

def six():
    pass

def seven():
    pass

def eight():
    pass

def nine():
    pass

def ten():
    pass

def eleven():
    pass

def twelve():
    pass

def selector(argument):
    switcher = {
        1: one,

    }
    # Get the function from switcher dictionary
    return switcher.get(argument, lambda: "Invalid selection.  Try again.")

def set_template_file(file_path):
    """
    Assumes
    from string import Template
    :param file_path: path to file which will contain a template
    :return: Template object
    """
    with open(file_path, 'r') as f:
        template_obj = Template(f.read())

    return template_obj

def ternary_operator_example():
    is_nice = True
    state = "nice" if is_nice else "not nice"