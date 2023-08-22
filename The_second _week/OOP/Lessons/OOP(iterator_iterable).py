"""
both of theme are related tools to iterate over a data stream or container.
Iterators power and control the iteration process,
while iterables typically hold data that you want to iterate over one value at a time.
Itarables can be changed to iterate.
same data types are iterable but it is not an iterator, like "STR".

"""
cities = ["Tehran","New York","Paris"]
# Create an object and change to iterator
iterator_obj = iter(cities)

# print (next(iterator_obj))
# print (next(iterator_obj))
# print (next(iterator_obj))

# # check iterable ir iterator
# print("__iter__" in dir(cities)) # iterable
# print("__next__" in dir(cities)) # not iterator
# # 

class Newobj:
    def __init__(self):
        self.items = [1,2,3,4,5]
    def __iter__(self):
        for i in self.items:
            yield i
        # we can't use return
    
change_to_iter = iter(Newobj())
next(change_to_iter)
next(change_to_iter) 
for i in change_to_iter:
    # print(i)
    pass
#  ----------------------------------------------------------------

class MaxPow:
    def __init__(self, max_pow) -> None:
        self.n = 0
        self.max_pow = max_pow
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max_pow:
            res = self.n ** 2
            self.n += 1
            return res
        else:
            raise StopIteration
n = MaxPow(5)
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n)) # to 25
# print(next(n)) # raise StopIteration
#  or we can use for (when for is used, iter is called)

n1 =MaxPow(5)
for i in n1:
    print(i)


