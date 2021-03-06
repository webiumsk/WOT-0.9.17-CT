# 2016.11.19 19:59:31 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/json/tests/test_speedups.py
from json.tests import CTest

class TestSpeedups(CTest):

    def test_scanstring(self):
        self.assertEqual(self.json.decoder.scanstring.__module__, '_json')
        self.assertIs(self.json.decoder.scanstring, self.json.decoder.c_scanstring)

    def test_encode_basestring_ascii(self):
        self.assertEqual(self.json.encoder.encode_basestring_ascii.__module__, '_json')
        self.assertIs(self.json.encoder.encode_basestring_ascii, self.json.encoder.c_encode_basestring_ascii)


class TestDecode(CTest):

    def test_make_scanner(self):
        self.assertRaises(AttributeError, self.json.scanner.c_make_scanner, 1)

    def test_make_encoder(self):
        self.assertRaises(TypeError, self.json.encoder.c_make_encoder, None, "\xcd}=N\x12L\xf9y\xd7R\xba\x82\xf2'J}\xa0\xcau", None)
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\Lib\json\tests\test_speedups.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:59:31 St�edn� Evropa (b�n� �as)
