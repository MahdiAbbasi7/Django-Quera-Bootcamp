import unittest
import functions
import traceback

from itertools import count, cycle

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

class OneTests(unittest.TestCase):
    def test_basic(self):
        it = ['item']
        self.assertEqual(functions.one(it), 'item')
    
    def test_to_short(self):
        it=[]
        for too_short, exc_type in [
            (None, ValueError),
            (IndexError, IndexError)
        ]:
            with self.subTest(too_short= too_short):
                try:
                    functions.one(it, too_short=too_short)
                except exc_type:
                    formatted_exc = traceback.format_exc()
                    self.assertIn('StopIteration', formatted_exc)
                    self.assertIn('The above exception was the direct cause', formatted_exc)
                else:
                    self.fail()
    
    def test_too_long(self):
        it = count()
        self.assertRaises(ValueError, lambda: functions.one(it))
        self.assertEqual(next(it), 2)
        self.assertRaises(
            OverflowError, lambda: functions.one(it, too_long= OverflowError)
        )

    def test_too_long_default_message(self):
        it = count()
        self.assertRaisesRegex(
            ValueError,
            'Expected exactly one itme in iterable, but got 0, 1, '
            'and perhaps more.',
            lambda: functions.one(it)
        )

class InterleaveTests(unittest.TestCase):
    def test_short(self):
        actual = list(functions.interleave([3,4,5],[6,7,8],[1,2]))
        expected = ['3', '6', '1', '4' , '7' , '2']
        self.assertEqual(actual, expected)
    def test_even(self):
        actual = list(functions.interleave([1,4,7],[2,5,8],[3,6,9]))
        expected = ['1', '2', '3', '4' , '5' , '6', '7', '8', '9']
        self.assertEqual(actual, expected)
    def test_complex(self):
        actual = list(functions.interleave([3,4,5],['A','B','C'],list(count())))
        expected = ['3', 'A', '0', '4' , 'B' , '1']
        self.assertEqual(actual, expected)

class RepeatEachTests(unittest.TestCase):
    def test_default(self):
        actual = list(functions.repeat_each('ABC'))
        expected = ['A', 'A', 'B', 'B', 'C', 'C']
        self.assertEqual(actual, expected)

    def test_basic(self):
        actual = list(functions.repeat_each('ABC', 3))
        expected = ['A', 'A', 'A','B', 'B', 'B','C', 'C','C']
        self.assertEqual(actual, expected)

    def test_empty(self):
        actual = list(functions.repeat_each([]))
        expected = []
        self.assertEqual(actual, expected)

    def test_no_repeat(self):
        actual = list(functions.repeat_each('ABC', 0))
        expected = []
        self.assertEqual(actual, expected)

    def test_negetive_repeat(self):
        actual = list(functions.repeat_each('ABC', -1))
        expected = []
        self.assertEqual(actual, expected)

    def test_infinte_repeat(self):
        repeater = list(functions.repeat_each(cycle('AB')))
        actual = functions.slice(repeater, 5)
        expected = ['A','A', 'B', 'B', 'A']
        self.assertEqual(actual, expected)

class StrictlyTests(unittest.TestCase):
    def test_basic(self):
        iterable = ['a', 'b', 'c', 'd', 'e', 'f']
        n = 6
        actual = functions.strictly(iterable, n)
        expected  = iterable
        self.assertEqual(actual, expected)

    def test_too_short_default(self):
        iterable = ['a', 'b', 'c', 'd']
        n = 5
        with self.assertRaises(ValueError) as exc:
            list(functions.strictly(iterable, n))
        self.assertEqual(
            'Too few item in iterrable (got 4)', exc.exception.args[0]
        )
    def test_too_long_defualt(self):
        iterable = ['a', 'b', 'c', 'd']
        n = 5
        with self.assertRaises(ValueError) as exc:
            list(functions.strictly(iterable, n))
        self.assertEqual(
            'too many items in iterable (got at least 4)', exc.exception.args[0]
        )
    def test_too_short_custom(self):
        call_count = 0
        def too_short(item_count):
            nonlocal call_count
            call_count += 1

        iterable = ['a', 'b', 'c', 'd'] 
        n = 6
        actual =[]

        for item in functions.strictly(iterable, n , too_short=too_short): # second too_short is a functions in line 236
            actual.append(item)
        expected  = ['a', 'b', 'c', 'd'] 
        self.assertEqual(actual, expected)
        self.assertEqual(call_count, 1)


    def test_too_long_custom(self):
        import logging

        iterable = ['a', 'b', 'c', 'd'] 
        n = 2
        too_long = lambda item_count:logging.warning(
            f'Picked the first {n} items'
        )
        
        with self.assertLogs(level='WARNING') as exc:
            actual = list(functions.strictly(iterable, n, too_long=too_long))
        self.assertEqual(actual, ['a', 'b'])
        self.assertIn('Picked the first 2 items', exc.output[0])

class OnlyTests(unittest.TestCase):
    def test_default(self):
        self.assertEqual(functions.only([]), None)
        self.assertEqual(functions.only([1]), 1)
        self.assertRaises(ValueError, lambda: functions.only([1, 2]))

    def test_custom_value(self):
        self.assertEqual(functions.only([], defualt='!'),'!')
        self.assertEqual(functions.only([1], defualt='!'), 1)
        self.assertRaises(ValueError, lambda: functions.only([1, 2], defualt='!'))

    def test_custom_exceptions(self):
        self.assertEqual(functions.only([], too_long=RuntimeError), None)
        self.assertEqual(functions.only([1], too_long=RuntimeError), 1)
        self.assertRaises(RuntimeError, lambda: functions.only([1, 2], too_long=RuntimeError))

    
    def test_default_exceptions_messages(self):
        self.assertRaisesRegex(
            ValueError,
            'Expected exactly one item in iterable but got foo, bar, and perhaps more.',
            functions.only(['foo', 'bar', 'boo'])
        )

class Always_reverseTests(unittest.TestCase):
    def test_regular_reversed(self):
        self.assertEqual(
            list(reversed(range(10))), list(functions.always_reverse(range(10)))
        )
        self.assertEqual(
            list(reversed([1, 2, 3, 4])), list(functions.always_reverse([1, 2, 3, 4]))
        )
        self.assertEqual(
            reversed([1, 2, 3, 4]).__class__, functions.always_reverse([1, 2, 3, 4]).__class__
        )
    
    def test_nonregular_reversed(self):
        self.assertEqual(
            list(reversed([1, 2, 3, 4])), list(functions.always_reverse(x for x in [1, 2, 3, 4]))
        )
        self.assertNotEqual(
            reversed((1, 2)).__class__, functions.always_reverse(x for x in (1, 2)).__class__
        )

class Always_iterableTests(unittest.TestCase):
    def test_single(self):
        self.assertEqual(list(functions.always_iterable(1)), [1])
    
    def test_string(self):
        # b'bar', b for convert to bytes.
        for obj in ['foo', b'bar', 'baz']:
            actual = list(functions.always_iterable(obj))
            expected = list(obj)
            self.assertEqual(actual, expected)
    
    def test_base_type(self):
        dict_obj = {'a':1, 'b':2}
        str_obj = '123'

        defualt_actual = list(functions.always_iterable(dict_obj))
        defualt_expected = list(str_obj)
        self.assertEqual(defualt_actual, defualt_expected)

        custom_actual = list(functions.always_iterable(dict_obj, base_type=dict))
        custom_expected = list(dict_obj)
        self.assertEqual(custom_actual, custom_expected)

        str_actual = list(functions.always_iterable(str_obj, base_type=None))
        str_expected = list(str_obj)
        self.assertEqual(str_actual, str_expected)

        custom_actual = list(functions.always_iterable(dict_obj, base_type=((dict,),)))
        custom_expected = list(dict_obj)
        self.assertEqual(custom_actual,custom_expected)

    def test_iterabels(self):
        self.assertEqual(functions.always_iterable([0, 1]), [0, 1])
        self.assertEqual(functions.always_iterable([0, 1], base_type=None), [0, 1])
        self.assertEqual(functions.always_iterable(iter('foo')), ['f', 'o', 'o'])
        self.assertEqual(functions.always_iterable([]), [])

    def test_none(self):
        self.assertEqual(functions.always_iterable(None), [])

    def test_generator(self):
        def _gen():
            yield 0
            yield 1
        self.assertEqual(list(functions.always_iterable(_gen())), [0, 1])

class Split_AfterTests(unittest.TestCase):
    def test_start_with_separator(self):
        actual = list(functions.split_after('xooxoo', lambda c: c == 'x'))
        expected = [['x'], ['o', 'o', 'x'], ['o', 'o']]
        self.assertEqual(actual, expected)

    def test_finish_with_separator(self):
        actual = list(functions.split_after('ooxoox', lambda c: c == 'x'))
        expected = [['o', 'o'], ['x'], ['o', 'o' , 'x']]
        self.assertEqual(actual, expected)

    def test_no_seperator(self):
        actual = list(functions.split_after('ooo', lambda c: c == 'x'))
        expected = [['o','o', 'o']]
        self.assertEqual(actual, expected)
        
    def test_max_split(self):
        for args, expected in [
            (
                ('a,b,c,d', lambda x: x == ',', -1),
                [['a', ','], ['b', ','], ['c', ','], ['d']]
            ),
            (
                ('a,b,c,d', lambda x: x == ',', 0),
                [['a', ',', 'b', ',', 'c', ',', 'd']]
            ),
            (
                ('a,b,c,d', lambda x: x == ',', 1),
                [['a', ','], ['b', ',', 'c', ',', 'd']]
            ),
            (
                ('a,b,c,d', lambda x: x == ',', 2),
                [['a', ','], ['b', ','],['c', ',', 'd']]
            ),
            (
                ('a,b,c,d', lambda x: x == ',', 10),
                [['a', ','], ['b', ','], ['c', ','], ['d']]                
            )
            (
                ('a,b,c,d', lambda x: x == '@', 2),    
                [['a', ',', 'b', ',', 'c', ',', 'd']]
            ),
            (
                ('a,b,c,d', lambda x: x != ',', 2),  
                [['a'], [',', 'b'], [',', 'c', ',', 'd']]
            )
        ]:
            actual = list(functions.split_after(*args))
            self.assertEqual(actual, expected)




if __name__ == "__main__":
    unittest.main()