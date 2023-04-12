
import pytest

pytestmark = [pytest.mark.smoke, pytest.mark.fe]

class TestFirstClass(object):

    @pytest.mark.tcid1
    def test_first_in_class(self):
        print("")
        print("First In Class")


    def test_second_in_class(self):
        print("Second In Class")