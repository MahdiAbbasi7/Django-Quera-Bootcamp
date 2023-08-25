""" 
This is first test for explain Regex in python.
mahdi abbasi
"""
import re as re
from pprint import pprint

my_text = "Hello, world!,hello"

prog = re.compile(pattern='h..lo', flags=re.IGNORECASE | re.DOTALL)

# res = prog.findall(my_text)
res = prog.finditer(my_text)


pprint(list(res))

#----------------------------------------------------------------

"""Validations for Email addresses"""

EmailAddress = """
abbasimahdi782@gmail.com
Good-bad.@yahoo.com
Nice-Bad.email.o 
"""

pattern = re.compile(pattern='^([\w\.\-]+)@([a-zA-Z]+)\.([a-zA-Z]{2,5})' ,flags= re.MULTILINE )

res =  pattern.finditer(EmailAddress)
pprint(list(res))