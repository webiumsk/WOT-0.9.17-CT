# 2016.11.19 19:51:31 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ReferralReferrerIntroWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ReferralReferrerIntroWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onClickApplyButton(self):
        self._printOverrideError('onClickApplyButton')

    def onClickHrefLink(self):
        self._printOverrideError('onClickHrefLink')

    def as_setDataS(self, data):
        """
        :param data: Represented by ReferralReferrerIntroVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\ReferralReferrerIntroWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:31 St�edn� Evropa (b�n� �as)
