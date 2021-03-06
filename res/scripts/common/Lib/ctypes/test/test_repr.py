# 2016.11.19 19:58:11 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/ctypes/test/test_repr.py
from ctypes import *
import unittest
subclasses = []
for base in [c_byte,
 c_short,
 c_int,
 c_long,
 c_longlong,
 c_ubyte,
 c_ushort,
 c_uint,
 c_ulong,
 c_ulonglong,
 c_float,
 c_double,
 c_longdouble,
 c_bool]:

    class X(base):
        pass


    subclasses.append(X)

class X(c_char):
    pass


class ReprTest(unittest.TestCase):

    def test_numbers(self):
        for typ in subclasses:
            base = typ.__bases__[0]
            self.assertTrue(repr(base(42)).startswith(base.__name__))
            self.assertEqual('<X object at', repr(typ(42))[:12])

    def test_char(self):
        self.assertEqual("c_char('x')", repr(c_char('x')))
        self.assertEqual('<X object at', repr(X('x'))[:12])


if __name__ == '__main__':
    unittest.main()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\Lib\ctypes\test\test_repr.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:58:11 St�edn� Evropa (b�n� �as)
