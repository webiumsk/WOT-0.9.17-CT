# 2016.11.19 19:47:48 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/Listeners.py
import weakref
_languageChangeListeners = []
_deviceListeners = []

def registerInputLangChangeListener(listener):
    global _languageChangeListeners
    _languageChangeListeners.append(weakref.ref(listener))


def registerDeviceListener(listener):
    _deviceListeners.append(weakref.ref(listener))


def handleInputLangChangeEvent():
    import GUI
    for listener in [ x() for x in _languageChangeListeners if x() is not None ]:
        if hasattr(listener, 'handleInputLangChangeEvent'):
            listener.handleInputLangChangeEvent()

    return True


def onRecreateDevice():
    for listener in [ x() for x in _deviceListeners if x() is not None ]:
        if hasattr(listener, 'onRecreateDevice'):
            listener.onRecreateDevice()

    return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\bwobsolete_helpers\PyGUI\Listeners.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:47:48 St�edn� Evropa (b�n� �as)
