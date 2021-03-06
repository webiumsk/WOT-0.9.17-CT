# 2016.11.19 19:55:34 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/wotdecorators.py
import inspect
from functools import update_wrapper
from debug_utils import LOG_WRAPPED_CURRENT_EXCEPTION, CRITICAL_ERROR
from time_tracking import LOG_TIME_WARNING
import time
import time_tracking

def noexcept(func):

    def wrapper(*args, **kwArgs):
        try:
            return func(*args, **kwArgs)
        except:
            LOG_WRAPPED_CURRENT_EXCEPTION(wrapper.__name__, func.__name__, func.func_code.co_filename, func.func_code.co_firstlineno + 1)

    return wrapper


def nofail(func):

    def wrapper(*args, **kwArgs):
        try:
            return func(*args, **kwArgs)
        except:
            LOG_WRAPPED_CURRENT_EXCEPTION(wrapper.__name__, func.__name__, func.func_code.co_filename, func.func_code.co_firstlineno + 1)
            CRITICAL_ERROR('Exception in no-fail code')

    return wrapper


def exposedtoclient(func):

    def wrapper(*args, **kwArgs):
        try:
            lastTick = time.time()
            result = func(*args, **kwArgs)
            timeSinceLastTick = time.time() - lastTick
            if timeSinceLastTick > time_tracking.DEFAULT_TIME_LIMIT:
                LOG_TIME_WARNING(timeSinceLastTick, context=(getattr(args[0], 'id', 0),
                 func.__name__,
                 args,
                 kwArgs))
            return result
        except:
            LOG_WRAPPED_CURRENT_EXCEPTION(wrapper.__name__, func.__name__, func.func_code.co_filename, func.func_code.co_firstlineno + 1)

    return wrapper


def singleton(cls):
    return cls()


def decorate(func, dec):
    argspec = inspect.getargspec(func)
    name = func.__name__
    signature = inspect.formatargspec(*argspec)
    params = inspect.formatargspec(formatvalue=(lambda value: ''), *argspec)
    source = 'def %s%s: return __dec%s\n' % (name, signature, params)
    code = compile(source, '<decorator-gen>', 'single')
    env = {'__dec': dec}
    eval(code, env)
    return update_wrapper(env[name], func)


def decorator(dec):

    def wrapper(func):
        return decorate(func, dec(func))

    return wrapper
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\wotdecorators.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:55:34 St�edn� Evropa (b�n� �as)
