# 2016.11.19 19:59:31 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/json/tests/test_pass2.py
from json.tests import PyTest, CTest
JSON = '\n[[[[[[[[[[[[[[[[[[["Not too deep"]]]]]]]]]]]]]]]]]]]\n'

class TestPass2(object):

    def test_parse(self):
        res = self.loads(JSON)
        out = self.dumps(res)
        self.assertEqual(res, self.loads(out))


class TestPyPass2(TestPass2, PyTest):
    pass


class TestCPass2(TestPass2, CTest):
    pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\Lib\json\tests\test_pass2.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:59:31 St�edn� Evropa (b�n� �as)
