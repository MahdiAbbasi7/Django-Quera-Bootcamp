"""
    traceback ==> print_exc, format_exc
    __cause__, __context__
"""

import traceback

# try :
#     print(number)
# except :
#     # traceback.print_exc()
#     res = traceback.format_exc()
#     print(res) # type of res is string and uses in tests.

#----------------------------------------------------------------
"""
__cause__ and __context__ is used to Ex1 in Ex2 (nested Exception) then information from Ex1 is lost.
but python save this information in __cause__ and __context__.
you can not change this information because it explicit. (in __context__)
if intialize __cause__ , __context__ will be empty and 

"""
# nested Exception
# try :
#     raise ValueError
# except Exception:
#     raise ImportError

# __cause__
# try :
#     raise ValueError("value error")
# except Exception:
#     raise ImportError('import error') from TypeError("type error")

# __context__
try:
    try :
        raise ValueError("value error")
    except Exception:
        raise ImportError('import error')
except Exception as two:
    print(two.__context__) # value error
    print(two.__cause__) # none because we are not initialized

