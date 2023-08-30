import unittest
import chancked

class SliceTests(unittest.TestCase):
    def test_sample_slice(self):
        t = chancked.slice(range(10), 4)
        self.assertEqual(t, [0, 1, 2, 3])

    def test_null_slice(self):
        t = chancked.slice(range(10), 0)
        self.assertEqual(t, [])

    def test_negative_slice(self):
        self.assertRaises(ValueError, lambda: chancked.slice(-3, range(10)))
    
    def test_too_much_number_slice(self):
        t = chancked.slice(range(5), 10)
        self.assertEqual(t, [0, 1, 2, 3, 4])
                         
class ChanckedTests(unittest.TestCase):
    def test_even(self):
        self.assertEqual(
            list(chancked.chancked_func(["ABCDEF"], 3)), [["A", "B", "C"], ["D", "E","F"]]
        )
    
    def test_odd(self):
        self.assertEqual(
            list(chancked.chancked_func(["ABCDE"], 3)), [["A", "B", "C"], ["D", "E"]]
        )
    def test_null(self):
        self.assertEqual(
            list(chancked.chancked_func(["ABCDE"], None)), [["A", "B", "C", "D", "E"]]
        )

    def test_strict_false(self):
        self.assertEqual(
            list(chancked.chancked_func("ABCDE", 3, strict=False)),
            [["A", "B", "C"], ["D", "E"]]   
        )

    def test_strict_true(self):
        def f():
            return list(chancked.chancked_func("ABCD", 3, strict=True))
        
        self.assertRaisesRegex(ValueError, "iterator is not devided by number.", f)
        self.assertEqual(
            list(chancked.chancked_func(["ABCDEF"], 3, strict=True)),
            [["A", "B", "C"], ["D", "E","F"]]
        )
    
    def test_strict_true_size(self):
        def f():
            return list(chancked.chancked_func("ABCD", None, strict=True))
        self.assertRaisesRegex(ValueError, "number must be a positive number and not none or negative.", f)

if __name__ == "__main__":
    unittest.main()