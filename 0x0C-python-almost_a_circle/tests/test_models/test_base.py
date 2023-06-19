#!/usr/bin/python3
"""Tests for the base.py module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase_instantiation(unittest.TestCase):
    """Testing istantiation of the Base Class"""

    def test_no_arg(self):
        """Caling the class without and id"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """Testing three Base objects with no args"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_none(self):
        """Testing for None(id is by default None"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """Test for when id is is explicitly passed"""
        self.assertEqual(15, Base(15).id)

    def test_nb_objects_after_unique_id(self):
        """Test of number of objects after previous object def with
        a unique id"""
        b1 = Base()
        b2 = Base(15)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_reassign_of_id(self):
        """Test value of of id after reassiging it another value"""
        b1 = Base(15)
        b1.id = 18
        self.assertEqual(b1.id, 18)

    def test_nb_objects_is_private(self):
        """Test that nb_object class attr is indeed private"""
        with self.assertRaises(AttributeError):
            print(Base(15).__nb_instances)

    def test_str_id(self):
        """Passing string as id"""
        self.assertEqual("hi", Base("hi").id)

    def test_float_id(self):
        """Passing float as id"""
        self.assertEqual(1.2, Base(1.2).id)

    def test_complex_id(self):
        """Passing comlex value as id"""
        self.assertEqual(complex(2), Base(complex(2)).id)

    def test_dict_id(self):
        """Passing a dictionary as id"""
        self.assertEqual({"hi": 1, "hey": 2}, Base({"hi": 1, "hey": 2}).id)

    def test_bool_id(self):
        """Passing bool value as id"""
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        """Passing a list as id"""
        self.assertEqual([1, 2, 3, 4], Base([1, 2, 3, 4]).id)

    def test_tuple_id(self):
        """Passing a tuple as id"""
        self.assertEqual((1, 2, 3), Base((1, 2, 3)).id)

    def test_set_id(self):
        """Passing a set as id"""
        self.assertEqual({1, 2, 3, 4}, Base({1, 2, 3, 4}).id)

    def test_frozenset_id(self):
        """Passing comlex value as id"""
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        """Passing range object(a sequence) as id"""
        self.assertEqual(range(2), Base(range(2)).id)

    def test_bytes_id(self):
        """Passing bytes value as id"""
        self.assertEqual(b'abc', Base(b'abc').id)

    def test_bytearray_id(self):
        """Passing byte array as id"""
        self.assertEqual(bytearray(b'abc'), Base(bytearray(b'abc')).id)

    def test_memoryview_id(self):
        """Tests if two objects refer to the same underlying memory """
        self.assertEqual(memoryview(b'abc'), Base(memoryview(b'abc')).id)

    def test_inf_id(self):
        """Passing infinity value as id"""
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        """Passing NaN value as id"""
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        """Pasing two values to Base"""
        with self.assertRaises(TypeError):
            Base(2, 3)


class TestBase_to_json_string(unittest.TestCase):
    """Test cases for to_json_string static method of the Base class"""

    def test_to_json_string_rectangle_type(self):
        """Testing if the return type is correct"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        """Passig one dictinary as value"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 52)

    def test_to_json_string_rectangle_two_dicts(self):
        """Passing two dictionaries"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        _dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(_dicts)) == 104)

    def test_to_json_string_square_type(self):
        """Testing if the return type is correct"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        """Passig one dictionary as value"""
        s = Square(1, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 38)

    def test_to_json_string_square_two_dicts(self):
        """Passig two dictionaries as value"""
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 3, 2, 1)
        _dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(_dicts)) == 76)

    def test_to_json_string_none(self):
        """Testing None value"""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        """Passing no value"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_two_args(self):
        """Passing two args, to_json_sting requires only one arg"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Test cases for save_to_file class method of the Base class"""

    @classmethod
    def tearDown(self):
        """Removes file created after each individual test"""
        file_names = ["Rectangle.json", "Square.json", "Base.json"]
        for file_name in file_names:
            try:
                os.remove(file_name)
            except IOError:
                pass

    def test_save_to_file_one_rectangle(self):
        """Passing one rectangle"""
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 52)

    def test_save_to_file_two_rectangles(self):
        """passing two rectangles"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 104)

    def test_save_to_file_one_square(self):
        """Passing one square"""
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_two_squares(self):
        """passing two squares"""
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 3, 2, 1)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 76)

    def test_save_to_file_with_base_class(self):
        """Passing one square"""
        s = Square(1, 2, 3, 4)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_overwrite(self):
        """Testing if it overites previous value when called again"""
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        s = Square(4, 3, 2, 1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_None(self):
        """Passing None as value"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        """Passing an empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        """Passing no args"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_two_args(self):
        """Passing two args"""
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Test cases for the statitic method from_json_string"""

    def test_from_json_string_type(self):
        """Testing for correct type after execution"""
        _input = [{"id": 1, "width": 2, "height": 3}]
        json_input = Rectangle.to_json_string(_input)
        _output = Rectangle.from_json_string(json_input)
        self.assertEqual(list, type(_output))

    def test_from_json_string_one_rectangle(self):
        """Passing one rect and testing input is same as output"""
        _input = [{"id": 1, "width": 2, "height": 3, "x": 4}]
        json_input = Rectangle.to_json_string(_input)
        _output = Rectangle.from_json_string(json_input)
        self.assertEqual(_input, _output)

    def test_from_json_string_two_rectangles(self):
        """Passing 2 rects and testing input is same as output"""
        _input = [
                {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                {"id": 5, "width": 4, "height": 3, "x": 2, "y": 1}
                    ]
        json_input = Rectangle.to_json_string(_input)
        _output = Rectangle.from_json_string(json_input)
        self.assertEqual(_input, _output)

    def test_from_json_string_one_square(self):
        """Passing one square and testing input is same as output"""
        _input = [{"id": 1, "size": 2, "x": 4}]
        json_input = Square.to_json_string(_input)
        _output = Square.from_json_string(json_input)
        self.assertEqual(_input, _output)

    def test_from_json_string_two_squares(self):
        """Passing 2 squares and testing input is same as output"""
        _input = [
                {"id": 1, "size": 2, "x": 4, "y": 5},
                {"id": 5, "size": 4, "x": 2, "y": 1}
                    ]
        json_input = Square.to_json_string(_input)
        _output = Square.from_json_string(json_input)
        self.assertEqual(_input, _output)

    def test_from_json_string_None(self):
        """Passing None as value"""
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_empty_list(self):
        """Passing an empty list"""
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        """Passing no args"""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_save_to_file_two_args(self):
        """Passing two args"""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Test cases for the classmethod crate() of the Base class"""

    def test_create_rectangle_orig(self):
        """creating new obj from an existing one and testint if
        the str rep of the two are still the same"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(r1))

    def test_create_rectangle_new(self):
        """Testing creating new Class and testing with itself"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(r2))

    def test_create_rectangle_equals(self):
        """Testing if the two objects points to ths same memory location"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)

    def test_create_rectangle_is(self):
        """Testing if the two objects with same args is not same"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r1, r2)

    def test_create_square_orig(self):
        """creating new object from an existing one and testing if
        the str rep of the two are still the same"""
        r1 = Square(1, 2, 3, 4)
        r1_dict = r1.to_dictionary()
        r2 = Square.create(**r1_dict)
        self.assertEqual("[Square] (4) 2/3 - 1", str(r1))

    def test_create_square_new(self):
        """Testing creating new object and testing with itself"""
        r1 = Square(1, 2, 3, 4)
        r1_dict = r1.to_dictionary()
        r2 = Square.create(**r1_dict)
        self.assertEqual("[Square] (4) 2/3 - 1", str(r2))

    def test_create_square_equals(self):
        """Testing if the two objects points to ths same memory location"""
        r1 = Square(1, 2, 3, 4)
        r1_dict = r1.to_dictionary()
        r2 = Square.create(**r1_dict)
        self.assertNotEqual(r1, r2)

    def test_create_square_is(self):
        """Testing if the two objects with same args is not same"""
        r1 = Rectangle(1, 2, 3, 4)
        r1_dict = r1.to_dictionary()
        r2 = Square.create(**r1_dict)
        self.assertIsNot(r1, r2)


class TestBase_load_from_file(unittest.TestCase):
    """Test cases for save_to_file class method of the Base class"""

    @classmethod
    def tearDown(self):
        """Removes file created after each individual test"""
        file_names = ["Rectangle.json", "Square.json"]
        for file_name in file_names:
            try:
                os.remove(file_name)
            except IOError:
                pass

    def test_load_from_file_first_rectangle(self):
        """Testing first Rectangle"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r1, r2])
        _output = Rectangle.load_from_file()
        self.assertEquals(str(r1), str(_output[0]))

    def test_load_from_file_second_rectangle(self):
        """Testing second Rectangle"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r1, r2])
        _output = Rectangle.load_from_file()
        self.assertEquals(str(r2), str(_output[1]))


    def test_load_from_file_rectangle_types(self):
        """Testing the type"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r1, r2])
        _output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in _output))

    def test_load_from_file_first_square(self):
        """Testing the first square"""
        r1 = Square(1, 2, 3, 4)
        r2 = Square(4, 3, 2, 1)
        Square.save_to_file([r1, r2])
        _output = Square.load_from_file()
        self.assertEquals(str(r1), str(_output[0]))

    def test_load_from_file_second_square(self):
        """Testing second Square"""
        r1 = Square(1, 2, 3, 4)
        r2 = Square(4, 3, 2, 1)
        Square.save_to_file([r1, r2])
        _output = Square.load_from_file()
        self.assertEquals(str(r2), str(_output[1]))


    def test_load_from_file_square_types(self):
        """Testing the type"""
        r1 = Square(1, 2, 3, 4)
        r2 = Square(4, 3, 2, 1)
        Square.save_to_file([r1, r2])
        _output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in _output))

    def test_load_from_file_no_file(self):
        """Testing for when there's no files"""
        _output = Square.load_from_file()
        self.assertEqual([], _output)

    def test_load_from_file_two_args(self):
        """Passing two args"""
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

if __name__ == "__main__":
    unittest.main()
