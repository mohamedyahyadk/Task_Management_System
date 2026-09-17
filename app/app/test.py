
from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
       
       def test_for_clalc(self):
            """test adding numbers together """
            res=calc.substract(5,10)
            self.assertEqual(res,5)
