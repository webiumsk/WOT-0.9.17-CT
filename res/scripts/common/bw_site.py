# 2016.11.19 19:55:11 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/bw_site.py
DEFAULT_ENCODING = 'utf-8'
import BWLogging
BWLogging.init()
import BigWorld
if BigWorld.component not in ('process_defs', 'client'):
    import BWUtil
    BWUtil.monkeyPatchOpen()
    import threading
    orig_bootstrap = threading.Thread._Thread__bootstrap

    def hooked_bootstrap(self):
        BigWorld.__onThreadStart(self.name)
        orig_bootstrap(self)
        BigWorld.__onThreadEnd()


    threading.Thread._Thread__bootstrap = hooked_bootstrap
import __builtin__
import pydoc

class _Helper(object):
    """Define the built-in 'help'.
    This is a wrapper around pydoc.help (with a twist).
    
    """

    def __repr__(self):
        return 'Type help() for interactive help, or help(object) for help about object.'

    def __call__(self, *args, **kwds):
        return pydoc.help(*args, **kwds)


def sethelper():
    __builtin__.help = _Helper()


import encodings
import sys

def setDefaultEncoding():
    if hasattr(sys, 'setdefaultencoding'):
        sys.setdefaultencoding(DEFAULT_ENCODING)
        del sys.setdefaultencoding
        import logging
        configLog = logging.getLogger('Config')
        configLog.info('Default encoding set to %s', sys.getdefaultencoding())


import os
import traceback
import ResMgr

def resMgrListDir(path, fnpat = None):
    """ResMgr stacked virtual file system directory listing. This is the
    union of the set of all files that exist in the matching path at
    each level of the stack.
    
    Optional shell style (not regex) file name filter pattern may be
    provided.
    
    If the path does NOT exist in any layer of the stacked vfs return
    None.
    """
    import fnmatch
    dir = ResMgr.openSection(path)
    if not dir:
        return dir
    if not fnpat:
        return dir.keys()
    return [ n for n in dir.keys() if fnmatch.fnmatch(n, fnpat) ]


def resMgrDirExists(path):
    """Predicate returns true if a data section (treated as a virtual dir)
    exists for the given path.
    """
    return ResMgr.openSection(path) != None


def getsitepackages():
    """Returns a list containing all global site-packages directories
    (and possibly site-python).
    
    For each directory present in the global ``PREFIXES``, this function
    will find its `site-packages` subdirectory depending on the system
    environment, and will return a list of full paths.
    """
    sitepackages = []
    seen = set()
    for prefix in sys.path:
        if not prefix or prefix in seen:
            continue
        seen.add(prefix)
        sitepackages.append(os.path.join(prefix, 'site-packages'))

    return sitepackages


def _init_pathinfo():
    """Return a set containing all existing directory entries from sys.path"""
    return set(sys.path)


def addpackage(sitedir, name, known_paths):
    """Process a .pth file within the site-packages directory:
       For each line in the file, either combine it with sitedir to a path
       and add that to known_paths, or execute it if it starts with 'import '.
    """
    if known_paths is None:
        _init_pathinfo()
        reset = 1
    else:
        reset = 0
    fullname = os.path.join(sitedir, name)
    try:
        f = open(fullname, 'rU')
    except IOError as e:
        print >> sys.stderr, 'ioerror', e, fullname
        return

    with f:
        for n, line in enumerate(f):
            if line.startswith('#'):
                continue
            try:
                if line.startswith(('import ', 'import\t')):
                    exec line
                    continue
                line = line.rstrip()
                dir = os.path.join(sitedir, line)
                if dir not in known_paths and resMgrDirExists(dir):
                    sys.path.append(dir)
                    known_paths.add(dir)
            except Exception as err:
                print >> sys.stderr, 'Error processing line {:d} of {}:\n'.format(n + 1, fullname)
                for record in traceback.format_exception(*sys.exc_info()):
                    for line in record.splitlines():
                        print >> sys.stderr, '  ' + line

                print >> sys.stderr, '\nRemainder of file ignored'
                break

    if reset:
        known_paths = None
    return known_paths


def addsitedir(sitedir, known_paths = None):
    """Add 'sitedir' argument to sys.path if missing and handle .pth files in
    'sitedir'"""
    if known_paths is None:
        known_paths = _init_pathinfo()
        reset = 1
    else:
        reset = 0
    if sitedir not in known_paths:
        sys.path.append(sitedir)
    names = resMgrListDir(sitedir, '*.pth')
    if names == None:
        return
    else:
        for name in sorted(names):
            addpackage(sitedir, name, known_paths)

        if reset:
            known_paths = None
        return known_paths


def addsitepackages(known_paths):
    """Add site-packages (and possibly site-python) to sys.path"""
    for sitedir in getsitepackages():
        if resMgrDirExists(sitedir):
            addsitedir(sitedir, known_paths)

    return known_paths


def setupPaths():
    known_paths = set(sys.path)
    known_paths = addsitepackages(known_paths)


def setTwistedReactor():
    """
    Override Twisted's default reactor, selectreactor, with ours.
    This ensures the only reactor installed is BWTwistedReactor.
    """
    if BigWorld.component in ('base', 'service', 'cell', 'database'):
        import BWTwistedReactor
        import twisted.internet.selectreactor
        twisted.internet.selectreactor = BWTwistedReactor


def main():
    sethelper()
    setDefaultEncoding()
    if BigWorld.component not in ('client', 'bot'):
        setupPaths()
    setTwistedReactor()
    import bwpydevd
    bwpydevd.startDebug(isStartUp=True)


main()
import bwdeprecations
from bwdebug import NOTICE_MSG
try:
    import BWAutoImport
except ImportError as e:
    NOTICE_MSG('bw_site.py failed to import BWAutoImport: %s\n' % (e,))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\bw_site.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:55:11 St�edn� Evropa (b�n� �as)
