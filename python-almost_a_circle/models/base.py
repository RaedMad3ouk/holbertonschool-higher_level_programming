#!/usr/bin/python3
"""Unittest class TestBase
"""
import unittest
from models.base import Base


class Test(unittest.TestCase):
    """ Class for testing Base
    """
    def setUp(self):
        Base._reset_nb_objects()

    def test_id_assignment(self):
        """ Tests first id assignment
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_increment(self):
        """ Tests id increment
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_override(self):
        """ Tests if id arg overrides increment
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_id_reverts(self):
        """ Tests if id increment reverts after override
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(33)
        self.assertEqual(b3.id, 33)
        b4 = Base()
        self.assertEqual(b4.id, 3)
            def create(cls, **dictionary):
        """ Returns an instance with all attrs set
        """
        pass
        dummy = cls(width=1, height=1, x=0, y=0, id=None)
        return(dummy.update(**dictionary))

    @classmethod
    def load_from_file(cls):
@@ -55,13 +56,22 @@ def load_from_file(cls):
    def save_to_file(cls, list_objs):
        """ Writes JSON string rep of list_objs to file
        """
        import json
        filename = cls.__name__
        dictlist = []
        dictlist2 = []
        for x in list_objs:
            dictlist.append(vars(x))
        with open("{}.json".format(filename), mode='w', encoding='utf-8') as f:
            f.write(Base.to_json_string(dictlist))
            newf = (Base.to_json_string(dictlist))
            newf = (newf.replace('_Rectangle__', ''))
            f.write(newf)
        # filename = cls.__name__
        # dictlist = []
        # dictlist2 = []
        # for x in list_objs:
        #     dictlist.append(vars(x))
        # with open("{}.json".format(filename), mode='w', encoding='utf-8') as
        #     f.write(Base.to_json_string(dictlist))

    @classmethod
    def _reset_nb_objects(cls):