import copy
import unittest
from selective_shallow_compare import selective_shallow_compare, find_all_different_attributes


class TestSelectiveShallowCompareForLists(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.list1 = [1, 2, 3]
        cls.list2 = [4, 5]

    def test_selective_shallow_compare(self):
        self.assertTrue(selective_shallow_compare(self.list1, self.list2, ['__class__', '__doc__', '__hash__',
                                                                           '__init_subclass__', '__new__',
                                                                           '__subclasshook__']))
        self.assertFalse(selective_shallow_compare(self.list1, self.list2, ['__format__']))
        self.assertFalse(selective_shallow_compare(self.list1, self.list2, ['__init__']))
        self.assertFalse(selective_shallow_compare(self.list1, self.list2, ['__sizeof__']))
        self.assertFalse(selective_shallow_compare(self.list1, self.list2, ['index']))

    def test_find_all_different_attributes(self):
        self.assertEqual(({'different': ['__add__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__eq__',
                                         '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
                                         '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__',
                                         '__lt__', '__mul__', '__ne__', '__reduce__', '__reduce_ex__', '__repr__',
                                         '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
                                         '__str__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
                                         'pop', 'remove', 'reverse', 'sort'],
                           'identical': ['__class__', '__doc__', '__hash__', '__init_subclass__', '__new__',
                                         '__subclasshook__']}),
                         find_all_different_attributes(self.list1, self.list2))


class TestSelectiveShallowCompareForDicts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dict1 = {'name': 'Johny', 'surname': 'Walker'}
        cls.dict2 = {'name': 'Jim', 'surname': 'Beam'}

    def test_selective_shallow_compare(self):
        self.assertTrue(selective_shallow_compare(self.dict1, self.dict2, ['__class__', '__doc__', '__hash__',
                                                                           '__init_subclass__', '__new__',
                                                                           '__subclasshook__', 'fromkeys']))
        self.assertFalse(selective_shallow_compare(self.dict1, self.dict2, ['__format__']))
        self.assertFalse(selective_shallow_compare(self.dict1, self.dict2, ['__init__']))
        self.assertFalse(selective_shallow_compare(self.dict1, self.dict2, ['__sizeof__']))
        self.assertFalse(selective_shallow_compare(self.dict1, self.dict2, ['__str__']))

    def test_find_all_different_attributes(self):
        self.assertEqual(({'different': ['__contains__', '__delattr__', '__delitem__', '__dir__', '__eq__',
                                         '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
                                         '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__reduce__',
                                         '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__',
                                         '__str__', 'clear', 'copy', 'get', 'items', 'keys', 'pop', 'popitem',
                                         'setdefault', 'update', 'values'],
                           'identical': ['__class__', '__doc__', '__hash__', '__init_subclass__', '__new__',
                                         '__subclasshook__', 'fromkeys']}),
                         find_all_different_attributes(self.dict1, self.dict2))


class TestSelectiveShallowCompareForCopiedLists(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.list1 = [1, 2, 3]
        cls.list2 = copy.deepcopy(cls.list1)

    def test_selective_shallow_compare(self):
        self.assertTrue(selective_shallow_compare(self.list1, self.list2, ['__class__', '__doc__', '__hash__',
                                                                           '__init_subclass__', '__new__',
                                                                           '__subclasshook__']))
        self.assertFalse(selective_shallow_compare(self.list1, self.list2, ['__format__']))
        self.assertFalse(selective_shallow_compare(self.list1, self.list2, ['__sizeof__']))
        self.assertFalse(selective_shallow_compare(self.list1, self.list2, ['index']))

    def test_find_all_different_attributes(self):
        self.assertEqual(({'different': ['__dir__', '__format__', '__getitem__', '__reduce__', '__reduce_ex__',
                                         '__reversed__', '__sizeof__', 'append', 'clear', 'copy', 'count', 'extend',
                                         'index', 'insert', 'pop', 'remove', 'reverse', 'sort'],
                           'identical': ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
                                         '__doc__', '__eq__', '__ge__', '__getattribute__', '__gt__', '__hash__',
                                         '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__',
                                         '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__repr__', '__rmul__',
                                         '__setattr__', '__setitem__', '__str__', '__subclasshook__']}),
                         find_all_different_attributes(self.list1, self.list2))


if __name__ == '__main__':
    unittest.main()
