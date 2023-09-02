import unittest
import functions
import traceback

class SliceTests(unittest.TestCase):
    def test_sample_slice(self):
        t = functions.slice(range(10), 4)
        self.assertEqual(t, [0, 1, 2, 3])

    def test_null_slice(self):
        t = functions.slice(range(10), 0)
        self.assertEqual(t, [])

    def test_negative_slice(self):
        self.assertRaises(ValueError, lambda: functions.slice(-3, range(10)))
    
    def test_too_much_number_slice(self):
        t = functions.slice(range(5), 10)
        self.assertEqual(t, [0, 1, 2, 3, 4])
                         
class ChanckedTests(unittest.TestCase):
    def test_even(self):
        self.assertEqual(
            list(functions.chancked_func("ABCDEF", 3)), [["A", "B", "C"], ["D", "E","F"]]
        )
    
    def test_odd(self):
        self.assertEqual(
            list(functions.chancked_func("ABCDE", 3)), [["A", "B", "C"], ["D", "E"]]
        )
    def test_null(self):
        self.assertEqual(
            list(functions.chancked_func("ABCDE", None)), [["A", "B", "C", "D", "E"]]
        )

    def test_strict_false(self):
        self.assertEqual(
            list(functions.chancked_func("ABCDE", 3, strict=False)),
            [["A", "B", "C"], ["D", "E"]]   
        )

    def test_strict_true(self):
        def f():
            return list(functions.chancked_func("ABCD", 3, strict=True))
        
        self.assertRaisesRegex(ValueError, "iterator is not devided by number.", f)
        self.assertEqual(
            list(functions.chancked_func("ABCDEF", 3, strict=True)),
            [["A", "B", "C"], ["D", "E","F"]]
        )
    
    def test_strict_true_size(self):
        def f():
            return list(functions.chancked_func("ABCDE", None, strict=True))
        self.assertRaisesRegex(
            ValueError, "number must be a positive number and not none or negative.", f
            )

class FirstTests(unittest.TestCase):
    def test_many(self):
        self.assertEqual(functions.first(x for x in range(4)), 0)
    
    def test_one(self):
        self.assertEqual(functions.first([3]),3)

    def test_default_value(self):
        self.assertEqual(functions.first([], "e"), "e")
   
    def test_not_default_value(self):
        # use traceback
        try:
            functions.first([])
        except ValueError:
            formatted_exec = traceback.format_exc() # change this to string.
            self.assertIn("StopIteration", formatted_exec)
            self.assertIn("The above exception was the direct cause", formatted_exec)
        else:
            self.fail()

class LastTests(unittest.TestCase):
    def test_basic(self):
        cases = [
            (range(4), 3),
            (iter(range(4)), 3),
            (range(1), 0),
            (iter(range(1)), 0),
            ({n: str(n) for n in range(5)}, 4)
        ]
        for iterable, expected in cases:
            with self.subTest(iterable=iterable):
                self.assertEqual(functions.last(iterable), expected)
    
    def test_default(self):
        for iterable, defualt, expected in [
            (range(1), None, 0),
            ([], None, None),
            ({}, None, None),
            (iter([]), None, None)
        ]:
            with self.subTest(iterable, defualt=defualt):
                self.assertEqual(functions.last(iterable, defualt), expected)

    def test_empty(self):
        for iterable in ([], iter(range(0))):
            with self.subTest(iterable=iterable):
                with self.assertRaises(ValueError):
                    functions.last(iterable) 

class Nth_or_lastTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(functions.nth_or_last([1,2,3,4], 2), 3)
        self.assertEqual(functions.nth_or_last([1,2,3,4], 6), 4)
    
    def test_defualt_value(self):
        defualt = 85
        self.assertEqual(functions.nth_or_last(range(5), 2 , defualt), 2)
        self.assertEqual(functions.nth_or_last([], 0 , defualt), defualt)
    
    def test_empty_iterable_no_defualt(self):
        """nabod lambda : vaghty test haro run koni onja ham behet error ro neshon mide."""
        self.assertRaises(ValueError, lambda: functions.nth_or_last(range(0), 5), )

if __name__ == "__main__":
    unittest.main()