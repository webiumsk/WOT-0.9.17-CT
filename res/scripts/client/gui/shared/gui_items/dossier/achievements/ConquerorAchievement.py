# 2016.11.19 19:52:48 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/ConquerorAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import ClassProgressAchievement
from abstract.mixins import Fortification

class ConquerorAchievement(Fortification, ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        ClassProgressAchievement.__init__(self, 'conqueror', _AB.FORT, dossier, value)

    def getNextLevelInfo(self):
        return ('fortDefResLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.FORT, 'conqueror')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getFortMiscStats().getLootInSorties()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\ConquerorAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:52:48 St�edn� Evropa (b�n� �as)
