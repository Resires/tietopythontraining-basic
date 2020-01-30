from pprint import pprint


def selective_shallow_compare(object1, object2, attributes_list):
    """Function that for given 2 objects and list of attribute names checks if objects' attributes are equal."""
    for attribute in attributes_list:
        if getattr(object1, attribute, 'not found') != getattr(object2, attribute, 'not found'):
            return False
    return True


def find_all_different_attributes(object1, object2):
    attributes_similarity = {'identical': [], 'different': []}
    for attribute in dir(object1):
        if selective_shallow_compare(object1, object2, [attribute]):
            attributes_similarity['identical'].append(attribute)
        else:
            attributes_similarity['different'].append(attribute)
    return attributes_similarity


def main():
    tested_object_1 = {'name': 'Johny', 'surname': 'Walker'}
    tested_object_2 = {'name': 'Jim', 'surname': 'Beam'}
    pprint(find_all_different_attributes(tested_object_1, tested_object_2))


if __name__ == '__main__':
    main()
