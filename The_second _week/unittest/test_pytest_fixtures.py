"""
Test for fixtures.
"""
import time 

import pytest
from fixtures import Person

class TestFixture:
    @pytest.fixture()
    def setUp(self):
        self.p1 = Person("mahdi", "abbasi")
        self.p2 = Person("john", "deo")
        yield "setUp" # after yield anything is a tear-down function.
        time.sleep(2)
        # you can not print anything...

    def test_fullname(self, setUp):
        assert self.p1.fullname() == "mahdi abbasi"
        assert self.p2.fullname() == "john deo"

    def test_email(self, setUp):
        assert self.p1.email() == "mahdiabbasi@gmail.com"
        assert self.p2.email() == "johndeo@gmail.com"
