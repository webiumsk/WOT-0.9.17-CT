# 2016.11.19 19:59:27 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/idlelib/idle_test/test_pathbrowser.py
import unittest
import idlelib.PathBrowser as PathBrowser

class PathBrowserTest(unittest.TestCase):

    def test_DirBrowserTreeItem(self):
        d = PathBrowser.DirBrowserTreeItem('')
        d.GetSubList()


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\Lib\idlelib\idle_test\test_pathbrowser.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:59:27 St�edn� Evropa (b�n� �as)
