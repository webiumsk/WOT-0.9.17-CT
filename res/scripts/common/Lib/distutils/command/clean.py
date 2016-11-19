# 2016.11.19 19:58:28 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/distutils/command/clean.py
"""distutils.command.clean

Implements the Distutils 'clean' command."""
__revision__ = '$Id$'
import os
from distutils.core import Command
from distutils.dir_util import remove_tree
from distutils import log

class clean(Command):
    description = "clean up temporary files from 'build' command"
    user_options = [('build-base=', 'b', "base build directory (default: 'build.build-base')"),
     ('build-lib=', None, "build directory for all modules (default: 'build.build-lib')"),
     ('build-temp=', 't', "temporary build directory (default: 'build.build-temp')"),
     ('build-scripts=', None, "build directory for scripts (default: 'build.build-scripts')"),
     ('bdist-base=', None, 'temporary directory for built distributions'),
     ('all', 'a', 'remove all build output, not just temporary by-products')]
    boolean_options = ['all']

    def initialize_options(self):
        self.build_base = None
        self.build_lib = None
        self.build_temp = None
        self.build_scripts = None
        self.bdist_base = None
        self.all = None
        return

    def finalize_options(self):
        self.set_undefined_options('build', ('build_base', 'build_base'), ('build_lib', 'build_lib'), ('build_scripts', 'build_scripts'), ('build_temp', 'build_temp'))
        self.set_undefined_options('bdist', ('bdist_base', 'bdist_base'))

    def run(self):
        if os.path.exists(self.build_temp):
            remove_tree(self.build_temp, dry_run=self.dry_run)
        else:
            log.debug("'%s' does not exist -- can't clean it", self.build_temp)
        if self.all:
            for directory in (self.build_lib, self.bdist_base, self.build_scripts):
                if os.path.exists(directory):
                    remove_tree(directory, dry_run=self.dry_run)
                else:
                    log.warn("'%s' does not exist -- can't clean it", directory)

        if not self.dry_run:
            try:
                os.rmdir(self.build_base)
                log.info("removing '%s'", self.build_base)
            except OSError:
                pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\Lib\distutils\command\clean.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:58:28 St�edn� Evropa (b�n� �as)
