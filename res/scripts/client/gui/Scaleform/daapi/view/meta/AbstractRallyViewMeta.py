# 2016.11.19 19:51:11 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AbstractRallyViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AbstractRallyViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setPyAliasS(self, alias):
        if self._isDAAPIInited():
            return self.flashObject.as_setPyAlias(alias)

    def as_getPyAliasS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getPyAlias()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\AbstractRallyViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:11 St�edn� Evropa (b�n� �as)
