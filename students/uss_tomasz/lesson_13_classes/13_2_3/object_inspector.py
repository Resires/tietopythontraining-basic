from pprint import pprint


def object_inspector_1(user_object):
    """Function that for a given object and list of attribute names returns dictionary with names and values of
    object's attributes"""
    names_and_values_of_obj_attr = {}
    for attribute in dir(user_object):
        names_and_values_of_obj_attr[attribute] = getattr(user_object, attribute, 'not found')
    return names_and_values_of_obj_attr


def object_inspector_2(user_object):
    """Function that for a given object returns dictionary with names and values of all object's attributes that are
    instances of string, integer or float."""
    names_and_values_of_obj_attr_inst_str_int_flt = {}
    for attribute in dir(user_object):
        if isinstance(attribute, (str, list, float)):
            names_and_values_of_obj_attr_inst_str_int_flt[attribute] = getattr(user_object, attribute, 'not found')
        return names_and_values_of_obj_attr_inst_str_int_flt


if __name__ == '__main__':
    a = 5
    b = [1, 2, 3]
    c = {'variable': 'value'}
    print('int, inspect 1')
    pprint(object_inspector_1(a))
    print('int, inspect 2')
    pprint(object_inspector_2(a))
    print('list, inspect 1')
    pprint(object_inspector_1(b))
    print('list, inspect 2')
    pprint(object_inspector_2(b))
    print('dict, inspect 1')
    pprint(object_inspector_1(c))
    print('dict, inspect 2')
    pprint(object_inspector_2(c))
