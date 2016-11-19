# 2016.11.19 19:47:47 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/FocusManager.py
_focusedComponent = None

def getFocusedComponent():
    global _focusedComponent
    return _focusedComponent


def setFocusedComponent(newFocus):
    global _focusedComponent
    if newFocus != _focusedComponent:
        if _focusedComponent is not None:
            _focusedComponent.focus = False
        _focusedComponent = newFocus
        if newFocus is not None:
            newFocus.focus = True
    return


def isFocusedComponent(component):
    if _focusedComponent is None or component is None:
        return _focusedComponent is component
    else:
        return _focusedComponent.__str__() == component.__str__()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\bwobsolete_helpers\PyGUI\FocusManager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:47:47 St�edn� Evropa (b�n� �as)
