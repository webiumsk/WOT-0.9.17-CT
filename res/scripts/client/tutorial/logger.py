# 2016.11.19 19:54:31 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/tutorial/logger.py
from constants import IS_DEVELOPMENT
from debug_utils import _doLog, LOG_CURRENT_EXCEPTION

class LOG_LEVEL:
    ERROR = 1
    WARNING = 2
    DEBUG = 4
    MEMORY = 8
    REQUEST = 16


CURRENT_LOG_LEVEL = LOG_LEVEL.ERROR
if IS_DEVELOPMENT:
    CURRENT_LOG_LEVEL |= LOG_LEVEL.WARNING
    CURRENT_LOG_LEVEL |= LOG_LEVEL.REQUEST

def LOG_DEBUG(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.DEBUG:
        _doLog('TUTORIAL DEBUG', msg, args)


def LOG_WARNING(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.WARNING:
        _doLog('TUTORIAL WARNING', msg, args)


def LOG_ERROR(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.ERROR:
        _doLog('TUTORIAL ERROR', msg, args)


def LOG_MEMORY(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.MEMORY:
        _doLog('TUTORIAL MEMORY', msg, args)


def LOG_REQUEST(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.REQUEST:
        _doLog('TUTORIAL REQUEST', msg, args)


__all__ = ('LOG_DEBUG', 'LOG_WARNING', 'LOG_ERROR', 'LOG_MEMORY', 'LOG_REQUEST', 'LOG_CURRENT_EXCEPTION')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\logger.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:54:31 St�edn� Evropa (b�n� �as)
