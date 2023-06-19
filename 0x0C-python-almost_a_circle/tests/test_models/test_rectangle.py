#!/usr/bin/python3
"""Tests for rectangle.py module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import sys


class TestRectangle_instantiation(unittest.TestCase):
    """Testing istantiation of the Rectangle Class"""

    def test_rectangle_isinstance_base(self):
        """Testing if rect obj is an instance of base class"""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_no_args(self):
        """Passing no arg"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Passing one argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Passing two arguments"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """Passing three arguments"""
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(2, 1, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """Passing four arguments"""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """Passing five arguments"""
        self.assertEqual(5, Rectangle(1, 2, 3, 4, 5).id)

    def test_more_than_five_args(self):
        """Passing more the five args"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        """Trying to access the width private value"""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__width)

    def test_height_private(self):
        """Trying to access the height private value"""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__height)

    def test_x_private(self):
        """Trying to access the x private value"""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__x)

    def test_y_private(self):
        """Trying to acess the y private value"""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__y)

    def test_width_getter(self):
        """Testing the getter method for width"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(1, r.width)

    def test_width_setter(self):
        """Testing the setter method for width"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 6
        self.assertEqual(6, r.width)

    def test_height_getter(self):
        """Testing the getter method for height"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(2, r.height)

    def test_height_setter(self):
        """Testing the setter method for height"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.height = 6
        self.assertEqual(6, r.height)

    def test_x_getter(self):
        """Testing the getter method for x"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(3, r.x)

    def test_x_setter(self):
        """Testing the setter method for x"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.x = 6
        self.assertEqual(6, r.x)

    def test_y_getter(self):
        """Testing the getter method for y"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(4, r.y)

    def test_y_setter(self):
        """Testing the setter method for y"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.y = 6
        self.assertEqual(6, r.y)

class TestRectangle_width(unittest.TestCase):
    """Test for the width attribute of Rectangle class"""

    def test_None_width(self):
        """Passing None as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        """Passing string as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hi", 2)

    def test_float_width(self):
        """Passing float as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.5, 2)

    def test_complex_width(self):
        """Passing complex as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(2), 2)

    def test_dict_width(self):
        """Passing dict as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"hi": 1, "hey": 2}, 2)

    def test_bool_width(self):
        """Passing bool as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        """Passing list as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle([1, 2], 2)

    def test_set_width(self):
        """Passing set as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle({1, 2}, 2)

    def test_tuple_width(self):
        """Passing tuple as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle((1, 2, 3, 4), 2)

    def test_frozenset_width(self):
        """Passing frozenset as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(frozenset({1, 2}), 2)

    def test_range_width(self):
        """Passing range as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(range(3), 2)

    def test_bytes_width(self):
        """Passing bytes as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(b'Hii', 2)

    def test_bytearray_width(self):
        """Passing bytearray as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(bytearray(b'abc'), 2)

    def test_memoryview_width(self):
        """Passing memoryview as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abc'), 2)

    def test_inf_width(self):
        """Passing inf as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(float('inf'), 2)

    def test_nan_width(self):
        """Passing nan as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(float('nan'), 2)

    def test_neg_width(self):
        """Passing negative value as width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Rectangle(-1, 2)

    def test_zero_width(self):
        """Passing zero as width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Rectangle(0, 2)

class TestRectangle_height(unittest.TestCase):
    """Test for the height attribute of Rectangle class"""

    def test_None_height(self):
        """Passing None as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        """Passing string as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "Hi")

    def test_float_height(self):
        """Passing float as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 1.5)

    def test_complex_height(self):
        """Passing complex as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(2))

    def test_dict_height(self):
        """Passing dict as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"hi": 1, "hey": 2})

    def test_bool_height(self):
        """Passing bool as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, True)

    def test_list_height(self):
        """Passing list as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(1, [1, 2])

    def test_set_height(self):
        """Passing set as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(1, {1, 2})

    def test_tuple_height(self):
        """Passing tuple as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(1, (1, 2, 3, 4))

    def test_frozenset_height(self):
        """Passing frozenset as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(1, frozenset({1, 2}))

    def test_range_height(self):
        """Passing range as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(1, range(3))

    def test_bytes_height(self):
        """Passing bytes as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(1, b'Hii')

    def test_bytearray_height(self):
        """Passing bytearray as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(1, bytearray(b'abc'))

    def test_memoryview_height(self):
        """Passing memoryview as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'abc'))

    def test_inf_height(self):
        """Passing inf as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(1, float('inf'))

    def test_nan_height(self):
        """Passing nan as height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(1, float('nan'))

    def test_neg_height(self):
        """Passing negative value as height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
                Rectangle(1, -1)

    def test_zero_height(self):
        """Passing zero as height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
                Rectangle(1, 0)

class TestRectangle_x(unittest.TestCase):
    """Test for the x attribute of Rectangle class"""

    def test_None_x(self):
        """Passing None as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        """Passing string as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "Hi")

    def test_float_x(self):
        """Passing float as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 1.5)

    def test_complex_x(self):
        """Passing complex as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(2))

    def test_dict_x(self):
        """Passing dict as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2,  {"hi": 1, "hey": 2})

    def test_bool_x(self):
        """Passing bool as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, True)

    def test_list_x(self):
        """Passing list as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, [1, 2])

    def test_set_x(self):
        """Passing set as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, {1, 2})

    def test_tuple_x(self):
        """Passing tuple as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, (1, 2, 3, 4))

    def test_frozenset_x(self):
        """Passing frozenset as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, frozenset({1, 2}))

    def test_range_x(self):
        """Passing range as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, range(3))

    def test_bytes_x(self):
        """Passing bytes as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, b'Hii')

    def test_bytearray_x(self):
        """Passing bytearray as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, bytearray(b'abc'))

    def test_memoryview_x(self):
        """Passing memoryview as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abc'))

    def test_inf_x(self):
        """Passing inf as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, float('inf'))

    def test_nan_x(self):
        """Passing nan as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, float('nan'))

    def test_neg_x(self):
        """Passing negative value as x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
                Rectangle(1, 2, -1)

class TestRectangle_y(unittest.TestCase):
    """Test for the y attribute of Rectangle class"""

    def test_None_y(self):
        """Passing None as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        """Passing string as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "Hi")

    def test_float_y(self):
        """Passing float as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 1.5)

    def test_complex_y(self):
        """Passing complex as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(2))

    def test_dict_y(self):
        """Passing dict as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {"hi": 1, "hey": 2})

    def test_bool_y(self):
        """Passing bool as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 3, True)

    def test_list_y(self):
        """Passing list as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, [1, 2])

    def test_set_y(self):
        """Passing set as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, {1, 2})

    def test_tuple_y(self):
        """Passing tuple as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, (1, 2, 3, 4))

    def test_frozenset_y(self):
        """Passing frozenset as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, frozenset({1, 2}))

    def test_range_y(self):
        """Passing range as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, range(3))

    def test_bytes_y(self):
        """Passing bytes as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, b'Hii')

    def test_bytearray_y(self):
        """Passing bytearray as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, bytearray(b'abc'))

    def test_memoryview_y(self):
        """Passing memoryview as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abc'))

    def test_inf_y(self):
        """Passing inf as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, float('inf'))

    def test_nan_y(self):
        """Passing nan as y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, float('nan'))

    def test_neg_y(self):
        """Passing negative value as y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
                Rectangle(1, 2, 3, -1)

class TestRectangle_order_of_initialization(unittest.TestCase):
    """Testcases for testing Rectangle order of attribute initialization."""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """Test cases for the area method of the Rectangle class."""

    def test_area_small(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_area_large(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_area_changed_attributes(self):
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """Tests cases for __str__ and display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.
        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test __str__ method
    def test_str_method_print_width_height(self):
        r = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # Test display method
    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Tests for update args method of the Rectangle class."""

    # Test args
    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Tests for update **kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Tests for to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        """Testing the output"""
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
