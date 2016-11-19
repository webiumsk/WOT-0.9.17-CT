# 2016.11.19 19:56:27 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/filecmp.py
"""Utilities for comparing files and directories.

Classes:
    dircmp

Functions:
    cmp(f1, f2, shallow=1) -> int
    cmpfiles(a, b, common) -> ([], [], [])

"""
import os
import stat
from itertools import ifilter, ifilterfalse, imap, izip
__all__ = ['cmp', 'dircmp', 'cmpfiles']
_cache = {}
BUFSIZE = 8192

def cmp(f1, f2, shallow = 1):
    """Compare two files.
    
    Arguments:
    
    f1 -- First file name
    
    f2 -- Second file name
    
    shallow -- Just check stat signature (do not read the files).
               defaults to 1.
    
    Return value:
    
    True if the files are the same, False otherwise.
    
    This function uses a cache for past comparisons and the results,
    with a cache invalidation mechanism relying on stale signatures.
    
    """
    s1 = _sig(os.stat(f1))
    s2 = _sig(os.stat(f2))
    if s1[0] != stat.S_IFREG or s2[0] != stat.S_IFREG:
        return False
    elif shallow and s1 == s2:
        return True
    elif s1[1] != s2[1]:
        return False
    else:
        outcome = _cache.get((f1,
         f2,
         s1,
         s2))
        if outcome is None:
            outcome = _do_cmp(f1, f2)
            if len(_cache) > 100:
                _cache.clear()
            _cache[f1, f2, s1, s2] = outcome
        return outcome


def _sig(st):
    return (stat.S_IFMT(st.st_mode), st.st_size, st.st_mtime)


def _do_cmp(f1, f2):
    bufsize = BUFSIZE
    with open(f1, 'rb') as fp1:
        with open(f2, 'rb') as fp2:
            while True:
                b1 = fp1.read(bufsize)
                b2 = fp2.read(bufsize)
                if b1 != b2:
                    return False
                if not b1:
                    return True


class dircmp:
    """A class that manages the comparison of 2 directories.
    
    dircmp(a,b,ignore=None,hide=None)
      A and B are directories.
      IGNORE is a list of names to ignore,
        defaults to ['RCS', 'CVS', 'tags'].
      HIDE is a list of names to hide,
        defaults to [os.curdir, os.pardir].
    
    High level usage:
      x = dircmp(dir1, dir2)
      x.report() -> prints a report on the differences between dir1 and dir2
       or
      x.report_partial_closure() -> prints report on differences between dir1
            and dir2, and reports on common immediate subdirectories.
      x.report_full_closure() -> like report_partial_closure,
            but fully recursive.
    
    Attributes:
     left_list, right_list: The files in dir1 and dir2,
        filtered by hide and ignore.
     common: a list of names in both dir1 and dir2.
     left_only, right_only: names only in dir1, dir2.
     common_dirs: subdirectories in both dir1 and dir2.
     common_files: files in both dir1 and dir2.
     common_funny: names in both dir1 and dir2 where the type differs between
        dir1 and dir2, or the name is not stat-able.
     same_files: list of identical files.
     diff_files: list of filenames which differ.
     funny_files: list of files which could not be compared.
     subdirs: a dictionary of dircmp objects, keyed by names in common_dirs.
     """

    def __init__(self, a, b, ignore = None, hide = None):
        self.left = a
        self.right = b
        if hide is None:
            self.hide = [os.curdir, os.pardir]
        else:
            self.hide = hide
        if ignore is None:
            self.ignore = ['RCS', 'CVS', 'tags']
        else:
            self.ignore = ignore
        return

    def phase0(self):
        self.left_list = _filter(os.listdir(self.left), self.hide + self.ignore)
        self.right_list = _filter(os.listdir(self.right), self.hide + self.ignore)
        self.left_list.sort()
        self.right_list.sort()

    def phase1(self):
        a = dict(izip(imap(os.path.normcase, self.left_list), self.left_list))
        b = dict(izip(imap(os.path.normcase, self.right_list), self.right_list))
        self.common = map(a.__getitem__, ifilter(b.__contains__, a))
        self.left_only = map(a.__getitem__, ifilterfalse(b.__contains__, a))
        self.right_only = map(b.__getitem__, ifilterfalse(a.__contains__, b))

    def phase2(self):
        self.common_dirs = []
        self.common_files = []
        self.common_funny = []
        for x in self.common:
            a_path = os.path.join(self.left, x)
            b_path = os.path.join(self.right, x)
            ok = 1
            try:
                a_stat = os.stat(a_path)
            except os.error as why:
                ok = 0

            try:
                b_stat = os.stat(b_path)
            except os.error as why:
                ok = 0

            if ok:
                a_type = stat.S_IFMT(a_stat.st_mode)
                b_type = stat.S_IFMT(b_stat.st_mode)
                if a_type != b_type:
                    self.common_funny.append(x)
                elif stat.S_ISDIR(a_type):
                    self.common_dirs.append(x)
                elif stat.S_ISREG(a_type):
                    self.common_files.append(x)
                else:
                    self.common_funny.append(x)
            else:
                self.common_funny.append(x)

    def phase3(self):
        xx = cmpfiles(self.left, self.right, self.common_files)
        self.same_files, self.diff_files, self.funny_files = xx

    def phase4(self):
        self.subdirs = {}
        for x in self.common_dirs:
            a_x = os.path.join(self.left, x)
            b_x = os.path.join(self.right, x)
            self.subdirs[x] = dircmp(a_x, b_x, self.ignore, self.hide)

    def phase4_closure(self):
        self.phase4()
        for sd in self.subdirs.itervalues():
            sd.phase4_closure()

    def report(self):
        print 'diff', self.left, self.right
        if self.left_only:
            self.left_only.sort()
            print 'Only in', self.left, ':', self.left_only
        if self.right_only:
            self.right_only.sort()
            print 'Only in', self.right, ':', self.right_only
        if self.same_files:
            self.same_files.sort()
            print 'Identical files :', self.same_files
        if self.diff_files:
            self.diff_files.sort()
            print 'Differing files :', self.diff_files
        if self.funny_files:
            self.funny_files.sort()
            print 'Trouble with common files :', self.funny_files
        if self.common_dirs:
            self.common_dirs.sort()
            print 'Common subdirectories :', self.common_dirs
        if self.common_funny:
            self.common_funny.sort()
            print 'Common funny cases :', self.common_funny

    def report_partial_closure(self):
        self.report()
        for sd in self.subdirs.itervalues():
            print
            sd.report()

    def report_full_closure(self):
        self.report()
        for sd in self.subdirs.itervalues():
            print
            sd.report_full_closure()

    methodmap = dict(subdirs=phase4, same_files=phase3, diff_files=phase3, funny_files=phase3, common_dirs=phase2, common_files=phase2, common_funny=phase2, common=phase1, left_only=phase1, right_only=phase1, left_list=phase0, right_list=phase0)

    def __getattr__(self, attr):
        if attr not in self.methodmap:
            raise AttributeError, attr
        self.methodmap[attr](self)
        return getattr(self, attr)


def cmpfiles(a, b, common, shallow = 1):
    """Compare common files in two directories.
    
    a, b -- directory names
    common -- list of file names found in both directories
    shallow -- if true, do comparison based solely on stat() information
    
    Returns a tuple of three lists:
      files that compare equal
      files that are different
      filenames that aren't regular files.
    
    """
    res = ([], [], [])
    for x in common:
        ax = os.path.join(a, x)
        bx = os.path.join(b, x)
        res[_cmp(ax, bx, shallow)].append(x)

    return res


def _cmp(a, b, sh, abs = abs, cmp = cmp):
    try:
        return not abs(cmp(a, b, sh))
    except (os.error, IOError):
        return 2


def _filter(flist, skip):
    return list(ifilterfalse(skip.__contains__, flist))


def demo():
    import sys
    import getopt
    options, args = getopt.getopt(sys.argv[1:], 'r')
    if len(args) != 2:
        raise getopt.GetoptError('need exactly two args', None)
    dd = dircmp(args[0], args[1])
    if ('-r', '') in options:
        dd.report_full_closure()
    else:
        dd.report()
    return


if __name__ == '__main__':
    demo()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\Lib\filecmp.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:56:28 St�edn� Evropa (b�n� �as)
