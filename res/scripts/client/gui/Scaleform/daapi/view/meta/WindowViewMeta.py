# 2016.11.19 19:51:37 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/WindowViewMeta.py
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class WindowViewMeta(WrapperViewMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends WrapperViewMeta
    """

    def onWindowMinimize(self):
        self._printOverrideError('onWindowMinimize')

    def onSourceLoaded(self):
        self._printOverrideError('onSourceLoaded')

    def onTryClosing(self):
        self._printOverrideError('onTryClosing')

    def as_getGeometryS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getGeometry()

    def as_setGeometryS(self, x, y, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_setGeometry(x, y, width, height)

    def as_isModalS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_isModal()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\WindowViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:37 St�edn� Evropa (b�n� �as)
